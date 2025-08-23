# 🤝 Contributing to Awesome Learn AI

Thank you for your interest in contributing to the Awesome Learn AI repository! This guide will help you make meaningful contributions to our community-driven AI learning resource.

## 🎯 Types of Contributions

### 📚 Content Contributions
- **New Learning Resources**: Add Microsoft Learn paths, modules, or labs
- **Content Updates**: Improve existing descriptions and information
- **Resource Organization**: Better categorization and structure
- **Translation**: Help translate content to other languages

### 🔧 Technical Contributions  
- **Documentation**: Improve setup guides and instructions
- **Tools**: Add helpful scripts or utilities
- **Bug Fixes**: Fix broken links or formatting issues
- **Accessibility**: Improve content accessibility

### 🌟 Community Contributions
- **Reviews**: Review pull requests from other contributors
- **Feedback**: Provide constructive feedback on content
- **Examples**: Share real-world project examples
- **Discussions**: Participate in community discussions

## 📋 Contribution Guidelines

### 🔍 Before Contributing

1. **Search Existing Content**: Check if your resource already exists
2. **Verify Quality**: Ensure resources are high-quality and relevant
3. **Check Links**: Verify all links are working and accessible
4. **Read Guidelines**: Familiarize yourself with our standards

### 📝 Content Standards

#### ✅ Acceptable Resources
- **Official Microsoft Learn content** (preferred)
- **High-quality, free educational resources**
- **Resources with clear learning outcomes**
- **Content from reputable sources**
- **Resources with proper documentation**

#### ❌ Not Acceptable
- **Broken or inaccessible links**
- **Paid-only content without free alternatives**
- **Outdated or deprecated resources**
- **Low-quality or incomplete content**
- **Resources requiring expensive tools/licenses**

#### 📏 Format Requirements

**Resource Entries Must Include:**
```markdown
| [Resource Title](https://link-to-resource) | Duration | Prerequisites | Description |
```

**Required Information:**
- **Title**: Clear, descriptive title
- **Link**: Working URL to official resource
- **Duration**: Realistic time estimate (e.g., "4-6 hours")
- **Prerequisites**: What learners need beforehand
- **Description**: 50-150 word clear description

#### 🎯 Difficulty Levels

- **🌱 Beginner**: No prior experience required
- **🌿 Intermediate**: Basic knowledge assumed
- **🌲 Advanced**: Significant experience required

## 🚀 How to Contribute

### 1️⃣ Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/awesome-learn-ai.git
cd awesome-learn-ai
```

### 2️⃣ Create Branch

```bash
# Create a new branch for your contribution
git checkout -b feature/your-contribution-name
```

### 3️⃣ Make Changes

- **Add Content**: Follow the existing markdown structure
- **Update Links**: Ensure all links work correctly
- **Test Format**: Preview your markdown changes
- **Follow Style**: Match existing formatting and tone

### 4️⃣ Commit Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "Add: [Resource Name] - Brief description"
```

**Commit Message Format:**
- `Add: [Resource Name] - Brief description`
- `Update: [Section] - What was changed`
- `Fix: [Issue] - What was fixed`
- `Docs: [Section] - Documentation changes`

### 5️⃣ Push & Create PR

```bash
# Push to your fork
git push origin feature/your-contribution-name
```

Then create a Pull Request on GitHub with:
- **Clear title** describing your contribution
- **Detailed description** of changes made
- **Checklist completion** (see template below)

## 📋 Pull Request Template

```markdown
## 📝 Description
Brief description of your changes and why they're valuable.

## 🔄 Type of Change
- [ ] ➕ New learning resource
- [ ] ✏️ Content update/improvement
- [ ] 🐛 Bug fix (broken link, typo, etc.)
- [ ] 📚 Documentation improvement
- [ ] 🌐 Translation
- [ ] 🏗️ Structure/organization improvement

## 📚 Resource Details (if adding new content)
- **Resource Title**: 
- **Source**: Microsoft Learn / Other
- **Difficulty Level**: Beginner/Intermediate/Advanced
- **Estimated Duration**: 
- **Prerequisites**: 
- **Key Technologies**: 

## ✅ Checklist
- [ ] I have read the contribution guidelines
- [ ] All links are working and accessible
- [ ] Content follows the established format
- [ ] Difficulty level is correctly assigned
- [ ] Duration estimate is realistic
- [ ] Description is clear and informative (50-150 words)
- [ ] Prerequisites are clearly listed
- [ ] No duplicate content
- [ ] Proper markdown formatting
- [ ] Spell-checked and grammar-checked

## 🧪 Testing
- [ ] Verified all links work (use `python scripts/validate_links.py`)
- [ ] Tested on mobile view
- [ ] Checked markdown rendering
- [ ] Validated content accuracy

## 🔗 Link Validation

Before submitting your PR, validate all links:

```bash
# Validate Microsoft Learn links
python scripts/validate_links.py

# Generate detailed report
python scripts/validate_links.py --output-report broken_links.md
```

The validation script will:
- ✅ Check all Microsoft Learn URLs  
- 📊 Provide summary statistics
- 📍 Show line numbers for broken links
- 💡 Suggest actions for fixing issues

## 📷 Screenshots (if applicable)
Include screenshots for UI changes or new sections.
```

## 🎨 Style Guide

### 📝 Writing Style
- **Clear and Concise**: Use simple, direct language
- **Consistent Tone**: Professional but approachable
- **Active Voice**: Prefer active over passive voice
- **Present Tense**: Use present tense for descriptions

### 🎭 Emoji Usage
- **Consistent**: Use emojis consistently across sections
- **Meaningful**: Each emoji should add meaning
- **Not Excessive**: Don't overuse emojis
- **Accessible**: Ensure content is readable without emojis

### 📊 Tables and Formatting
- **Aligned Columns**: Keep table columns properly aligned
- **Consistent Headers**: Use same header structure
- **Proper Spacing**: Maintain consistent spacing
- **Readable**: Ensure tables are easy to read

#### 🔗 Link Validation Guidelines

To maintain high-quality, working links:

1. **Always validate links** before submitting:
   ```bash
   python scripts/validate_links.py
   ```

2. **Replace broken links** with working alternatives:
   - Search Microsoft Learn for updated content
   - Use the most current URL structure
   - Prefer learning paths over individual modules when available

3. **Avoid tracking parameters** in URLs:
   - ❌ Bad: `https://learn.microsoft.com/path?wt.mc_id=tracking`
   - ✅ Good: `https://learn.microsoft.com/path`

4. **Common URL patterns** on Microsoft Learn:
   - Learning Paths: `/training/paths/[path-name]/`
   - Modules: `/training/modules/[module-name]/`
   - Browse: `/training/browse/`

5. **When links break**:
   - Check if content was moved or renamed
   - Look for successor content
   - Remove if permanently deprecated
   - Update description if content changed

6. **Duration accuracy**:
   - Verify time estimates match actual content
   - Use format: "X hours Y min" or "X-Y hours"
   - Check Microsoft Learn page for official duration

## 🔍 Review Process

### 📝 Review Criteria
1. **Accuracy**: Content is factually correct
2. **Quality**: High-quality, valuable resource
3. **Format**: Follows established guidelines
4. **Links**: All links work and are accessible
5. **Relevance**: Fits within repository scope

### ⏱️ Review Timeline
- **Initial Review**: Within 48 hours
- **Feedback Incorporation**: 7 days for contributor response
- **Final Review**: Within 24 hours of updates
- **Merge**: After approval from maintainers

### 👥 Reviewers
- **Maintainers**: Core team members
- **Community**: Experienced contributors
- **Subject Experts**: Domain specialists when needed

## 🐛 Reporting Issues

### 🔗 Broken Links
```markdown
**Issue**: Broken Link
**Resource**: [Resource Name]
**Link**: [Broken URL]
**Expected**: Working link to resource
**Actual**: 404 error / redirect / etc.
```

### 📝 Content Issues
```markdown
**Issue**: Content Problem
**Section**: [Section Name]
**Problem**: [Describe the issue]
**Suggestion**: [Proposed fix]
```

### 💡 Feature Requests
```markdown
**Feature**: [Feature Name]
**Description**: [What you'd like to see]
**Use Case**: [Why it would be valuable]
**Implementation**: [Ideas for how to implement]
```

## 🏆 Recognition

### 👤 Contributors
All contributors are recognized in our README.md and receive:
- **GitHub Profile Link**: In contributors section
- **Contribution Count**: Number of accepted contributions
- **Special Recognition**: For significant contributions

### 🎖️ Top Contributors
Outstanding contributors may receive:
- **Maintainer Status**: Help manage the repository
- **Special Badges**: Recognition in profile
- **LinkedIn Recommendations**: Professional recognition

## 📞 Getting Help

### 💬 Community Support
- **GitHub Discussions**: Ask questions and share ideas
- **Issues**: Report bugs or request features
- **Discord** (if available): Real-time community chat

### 📚 Resources
- **Markdown Guide**: [Markdown Syntax](https://www.markdownguide.org/)
- **GitHub Help**: [GitHub Documentation](https://docs.github.com/)
- **Microsoft Learn**: [Microsoft Learn Platform](https://learn.microsoft.com/)

### 🤝 Direct Contact
For urgent issues or sensitive matters:
- **Email**: [maintainer-email]
- **Twitter**: [@username]
- **LinkedIn**: [profile-link]

---

## 🙏 Thank You

Your contributions help make AI education accessible to learners worldwide. Every addition, fix, and improvement makes a difference in someone's learning journey.

**Happy Contributing! 🚀🤖**

---

*This contributing guide is living document and will be updated based on community feedback and needs.*