# CLAUDE.md - Project Guidelines and Rules

## Project Overview
This project involves deep analysis and documentation of the Synology SRM (Synology Router Manager) system. The goal is to create comprehensive, consistent, and professional documentation by analyzing every directory, file, and component in the srm_backup folder.

## MCP Tools Usage Guidelines

### 1. Zen MCP Tools
Use these tools for deep analysis, code review, and collaborative thinking:

- **mcp__zen__thinkdeep**: Use for complex analysis requiring deep reasoning
  - Use `pro` model with `high` or `max` thinking mode for architecture analysis
  - Use `flash` for quick queries
  - Always enable web search for best practices

- **mcp__zen__analyze**: For file and code analysis
  - Use for understanding system components
  - Analyze directories and configuration files
  - Pattern detection in system structure

- **mcp__zen__chat**: For collaborative thinking
  - Brainstorm documentation approaches
  - Validate documentation strategies
  - Get second opinions on complex topics

- **mcp__zen__consensus**: Get multiple AI perspectives
  - Use for important architectural decisions
  - Validate documentation approaches
  - Ensure comprehensive coverage

- **mcp__zen__planner**: For sequential planning
  - Break down complex documentation tasks
  - Plan analysis strategies
  - Organize documentation structure

### 2. Task Master Usage
Task Master is the primary task management system:

- **Always use Task Master** for task tracking and organization
- Break down work into:
  - Epics: Major documentation sections
  - User Stories: Specific documentation needs
  - Tasks: Individual analysis/documentation items
  - Subtasks: Detailed implementation steps

- **Workflow**:
  1. Create PRD for documentation goals
  2. Parse PRD to generate initial tasks
  3. Expand tasks based on complexity
  4. Track progress systematically
  5. Update tasks with findings

### 3. When to Use Subagents
Use the Task tool for subagents when:
- Searching for specific patterns across multiple files
- Performing repetitive analysis tasks
- Gathering information from many locations
- Parallel processing is beneficial

## Documentation Standards

### 1. Consistency Rules
- All documentation files in same scope must follow identical structure
- Use consistent formatting and sections
- Maintain uniform depth of analysis
- Apply same categorization methods

### 2. Documentation Structure
Each documentation file should include:
```markdown
# [Component Name]

## Overview
Brief description of the component's purpose and role in SRM

## Directory Structure
Detailed tree view of subdirectories and key files

## Key Components
### [Component Category]
- **Purpose**: What it does
- **Location**: Where it's found
- **Dependencies**: What it relies on
- **Configuration**: How it's configured
- **Security**: Security implications

## Configuration Files
Detailed analysis of configuration files

## Scripts and Executables
Analysis of scripts, their purpose, and usage

## Integration Points
How this component interacts with others

## Security Considerations
Security implications and best practices

## Network Services
If applicable, network services exposed

## Maintenance Notes
Important information for system maintenance
```

### 3. Analysis Depth
- **Level 1**: Directory purpose and structure
- **Level 2**: File categorization and relationships
- **Level 3**: Configuration analysis and dependencies
- **Level 4**: Security implications and integration points
- **Level 5**: Performance considerations and optimization

## Best Practices

### 1. Analysis Approach
- Start with high-level overview
- Progressively dive deeper
- Document relationships between components
- Identify security implications
- Note performance considerations

### 2. Documentation Quality
- Be precise and technical
- Include examples where helpful
- Cross-reference related components
- Maintain professional tone
- Ensure completeness

### 3. Tool Selection
- Use `gemini-2.5-pro` for deep analysis
- Use `gemini-2.5-flash` for quick checks
- Always use high thinking mode for complex analysis
- Enable web search for best practices

## Workflow Rules

### 1. Task Management
- Create tasks before starting work
- Update task status in real-time
- Document findings in tasks
- Complete subtasks systematically

### 2. Analysis Process
1. Use Task Master to create analysis tasks
2. Use Zen tools for deep analysis
3. Document findings consistently
4. Review with consensus tool
5. Update documentation files

### 2.1 Directory Analysis Workflow (Updated 2025-06-23)
For directory analysis tasks, follow this specific workflow:

1. **Initial Analysis with Zen Gemini**
   - Use `mcp__zen__analyze` with Gemini model for directory analysis
   - Let Gemini perform the complete directory exploration
   - Do NOT analyze directories manually

2. **Review and Verification**
   - Receive the analysis from Gemini
   - Review the findings for completeness and accuracy
   - Verify key findings if needed

3. **Documentation Generation**
   - Use Gemini again to create the full documentation content
   - If Gemini can write files directly, let it do so
   - Otherwise, take the generated content and save it yourself

4. **Benefits of this approach**:
   - Leverages Gemini's comprehensive analysis capabilities
   - Ensures consistent depth of analysis
   - Reduces manual work and potential oversights
   - Maintains high quality documentation standards

### 3. Quality Assurance
- Review each documentation file
- Ensure consistency across files
- Validate technical accuracy
- Check for completeness
- Verify security considerations

## Current Project Goals

### Primary Objectives
1. Complete deep analysis of entire SRM system
2. Create comprehensive documentation for each component
3. Ensure documentation consistency
4. Identify security implications
5. Map system architecture

### Task Breakdown
- [x] Initialize Task Master project
- [x] Create comprehensive PRD
- [x] Generate and expand tasks
- [x] Configure tags for task organization
- [ ] Analyze each directory systematically
- [ ] Create consistent documentation
- [ ] Review and refine documentation
- [ ] Ensure cross-references are complete

## Task Delegation Strategy

### Parallel Processing with Subagents
Tasks suitable for parallel delegation using the Task tool:

1. **Directory Analysis Tasks** (can run in parallel):
   - Task 7: /sbin analysis
   - Task 8: /bin analysis  
   - Task 9: /lib and /lib64 analysis
   - Task 10: /libexec analysis
   - Task 16: /data analysis
   - Task 17: /mnt analysis
   - Task 18: /root analysis

2. **Configuration Analysis** (sequential but can parallelize subtasks):
   - Task 3 subtasks: Network, Firewall, Services configs (parallel)
   - Task 4: /etc.defaults analysis after /etc

3. **High-Priority Sequential Tasks**:
   - Task 2: Template creation (must complete first)
   - Task 5: Security analysis (needs overview)
   - Task 6: Network services inventory
   - Task 20: Architecture synthesis (needs all data)

### Task Tags
- **security**: Tasks 3, 4, 5, 6, 11, 21
- **network**: Tasks 3.1, 3.2, 6, 12
- **config**: Tasks 3, 4, 14, 21
- **parallel**: Tasks 7, 8, 9, 10, 16, 17, 18

## Command Reference

### Useful Commands
- Check lint/typecheck: (to be determined based on project)
- Run tests: (to be determined based on project)
- Build documentation: (to be determined based on project)

## Notes
- This is a system analysis project, not code development
- Focus on understanding and documenting
- Security analysis is critical
- Performance implications matter
- Consistency is paramount

---
Last Updated: 2025-06-23