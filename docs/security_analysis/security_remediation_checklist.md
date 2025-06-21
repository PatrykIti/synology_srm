# Synology SRM Security Remediation Checklist

## Critical Priority (Immediate - Within 24 hours)

### ☐ 1. Enable DoS Protection
```bash
# Edit /etc/fw_security/global.conf
dos_protect_enable=yes

# Apply changes
synoservice --restart firewall
```

### ☐ 2. Disable PPTP Passthrough
```bash
# Remove PPTP rules from firewall
iptables -D VPN_PASSTHROUGH -p tcp --dport 1723 -j RETURN
iptables -D VPN_PASSTHROUGH -p 47 -j RETURN
ip6tables -D VPN_PASSTHROUGH -p tcp --dport 1723 -j RETURN
ip6tables -D VPN_PASSTHROUGH -p 47 -j RETURN

# Update configuration
sed -i 's/pptp_passthrough_enable=yes/pptp_passthrough_enable=no/g' /etc/fw_security/global.conf
```

### ☐ 3. Implement Emergency Access Control
```bash
# Create whitelist for VPN access
iptables -N VPN_WHITELIST
iptables -I VPN_PASSTHROUGH 1 -j VPN_WHITELIST
iptables -A VPN_WHITELIST -s <trusted_network>/24 -j RETURN
iptables -A VPN_WHITELIST -j DROP
```

## High Priority (Within 1 week)

### ☐ 4. Configure DoS Protection Parameters
```bash
# Add to /etc/sysctl.conf
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_fin_timeout = 30
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.rp_filter = 1

# Apply settings
sysctl -p
```

### ☐ 5. Add Connection Rate Limiting
```bash
# IPSec rate limiting
iptables -I INPUT -p udp --dport 500 -m recent --name ipsec --update --seconds 60 --hitcount 20 -j DROP
iptables -I INPUT -p udp --dport 500 -m recent --name ipsec --set

# L2TP rate limiting
iptables -I INPUT -p udp --dport 1701 -m recent --name l2tp --update --seconds 60 --hitcount 10 -j DROP
iptables -I INPUT -p udp --dport 1701 -m recent --name l2tp --set
```

### ☐ 6. Enable Comprehensive Logging
```bash
# Create logging rules
iptables -N LOG_AND_DROP
iptables -A LOG_AND_DROP -j LOG --log-prefix "FW_DROP: " --log-level 4
iptables -A LOG_AND_DROP -j DROP

# Apply to VPN rules
iptables -I VPN_PASSTHROUGH -j LOG --log-prefix "VPN_ACCESS: " --log-level 6

# Configure rsyslog
echo "kern.warning /var/log/firewall.log" >> /etc/rsyslog.conf
systemctl restart rsyslog
```

### ☐ 7. Harden L2TP Configuration
```bash
# Require IPSec for L2TP
iptables -I VPN_PASSTHROUGH -p udp --dport 1701 -m policy --dir in --pol none -j DROP
ip6tables -I VPN_PASSTHROUGH -p udp --dport 1701 -m policy --dir in --pol none -j DROP
```

## Medium Priority (Within 2 weeks)

### ☐ 8. IPv6 Security Hardening
```bash
# Disable unnecessary IPv6 features
echo "net.ipv6.conf.all.accept_ra = 0" >> /etc/sysctl.conf
echo "net.ipv6.conf.all.accept_redirects = 0" >> /etc/sysctl.conf
echo "net.ipv6.conf.all.accept_source_route = 0" >> /etc/sysctl.conf

# Block dangerous IPv6 types
ip6tables -A INPUT -m rt --rt-type 0 -j DROP
ip6tables -A INPUT -p ipv6-icmp --icmpv6-type 139 -j DROP
```

### ☐ 9. Implement GeoIP Filtering
```bash
# Install xtables-addons
apt-get install xtables-addons-common

# Download GeoIP database
/usr/lib/xtables-addons/xt_geoip_dl
/usr/lib/xtables-addons/xt_geoip_build

# Allow only specific countries
iptables -A INPUT -m geoip ! --src-cc US,CA,GB -j DROP
```

### ☐ 10. Configure IPSec Strong Ciphers
```
# /etc/ipsec.conf
config setup
    charondebug="all"
    uniqueids=yes
    strictcrlpolicy=no

conn %default
    ike=aes256-sha256-modp2048!
    esp=aes256-sha256!
    keyexchange=ikev2
    ikelifetime=24h
    lifetime=8h
```

## Monitoring and Maintenance

### ☐ 11. Set Up Monitoring Alerts
```bash
# Create monitoring script
cat > /usr/local/bin/vpn_monitor.sh << 'EOF'
#!/bin/bash
# Check for suspicious VPN activity
tail -n 1000 /var/log/firewall.log | grep "VPN_ACCESS" | \
awk '{print $NF}' | sort | uniq -c | sort -nr | \
while read count ip; do
    if [ $count -gt 50 ]; then
        echo "Alert: $ip made $count VPN attempts" | \
        mail -s "VPN Security Alert" admin@example.com
    fi
done
EOF

chmod +x /usr/local/bin/vpn_monitor.sh

# Add to crontab
echo "*/5 * * * * /usr/local/bin/vpn_monitor.sh" | crontab -
```

### ☐ 12. Create Backup of Secure Configuration
```bash
# Backup current rules
iptables-save > /etc/firewall_backup_$(date +%Y%m%d).rules
ip6tables-save > /etc/firewall6_backup_$(date +%Y%m%d).rules

# Create restore script
cat > /usr/local/bin/restore_firewall.sh << 'EOF'
#!/bin/bash
iptables-restore < /etc/firewall_backup_secure.rules
ip6tables-restore < /etc/firewall6_backup_secure.rules
EOF
chmod +x /usr/local/bin/restore_firewall.sh
```

## Verification Steps

### ☐ 13. Test DoS Protection
```bash
# From external host (controlled test)
hping3 -S -p 80 --flood --rand-source <target_ip>
# Should see connection limiting in logs
```

### ☐ 14. Verify VPN Restrictions
```bash
# Test from unauthorized IP
nc -u <target_ip> 500
# Should be blocked

# Test from authorized IP
nc -u <target_ip> 500
# Should connect
```

### ☐ 15. Audit Log Files
```bash
# Check for any bypass attempts
grep -E "(PPTP|1723|protocol=47)" /var/log/firewall.log
# Should return no active PPTP connections
```

## Regular Maintenance Schedule

### Daily
- ☐ Review firewall logs for anomalies
- ☐ Check active VPN connections

### Weekly  
- ☐ Update GeoIP database
- ☐ Review and update whitelist IPs
- ☐ Check for security updates

### Monthly
- ☐ Full security audit
- ☐ Update firewall rules based on new threats
- ☐ Test backup and restore procedures

## Emergency Contacts

- Security Team: security@company.com
- Network Admin: netadmin@company.com  
- Incident Response: +1-XXX-XXX-XXXX

---

**Important**: Save this checklist and mark items as completed. Keep a record of all changes made for compliance and rollback purposes.