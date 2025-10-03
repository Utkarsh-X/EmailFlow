# EmailFlow

<div align="center">
  <img width="1536" height="520" alt="logo" src="https://github.com/user-attachments/assets/0c23f79f-62f8-4dfc-b157-047633a75273" />

  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![Version](https://img.shields.io/badge/version-1.5.01-green.svg)](https://github.com/Utkarsh-X/EmailFlow/releases)
  [![Status](https://img.shields.io/badge/status-active-success.svg)]()

  **A powerful desktop application for automated email management and batch PDF processing**
</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Quick Start Guide](#-quick-start-guide)
- [Detailed Usage](#-detailed-usage)
- [Configuration](#-configuration)
- [Technical Stack](#-technical-stack)
- [Project Architecture](#-project-architecture)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Contact & Support](#-contact--support)

---

## 🎯 Overview

### The Problem

Back in late 2023, I faced a recurring challenge: sending batches of documents via email with specific quality requirements and automated workflows. Traditional email clients fell short—they lacked the ability to:
- Convert PDFs to high-resolution images with precise DPI control
- Process multiple files from folders automatically
- Maintain consistent formatting and subject lines
- Remember preferences for repetitive tasks
- Provide the level of customization needed for professional document handling

Existing solutions were either too simplistic (basic email clients), too expensive (enterprise automation tools), or didn't address the specific combination of features I needed. I wanted a tool that could handle automated email sending, high-quality image conversion, and smart file management—all in one place, with full control over every aspect.

So I built EmailFlow—not just to solve my immediate problem, but as a learning journey to deeply understand Python development, GUI design, SMTP protocols, file processing, and user experience principles. Building this from scratch taught me how these systems work at a fundamental level, far beyond what tutorials could provide.

The application was ready well before its public release. After refining the interface and adding customization features based on real-world use, I decided to publish it on GitHub to help others facing similar challenges while sharing what I learned along the way.

### The Solution

EmailFlow is an open-source Python desktop application that streamlines repetitive email and file management workflows. Originally created for my own needs, it evolved into a comprehensive solution that I'm now sharing with the community. Built for professionals, students, and anyone who regularly sends batches of files via email, it combines three essential functionalities into one intuitive interface:

- **Automated Email Sending** with SMTP support and recipient management
- **Batch PDF to Image Conversion** with precise DPI control (10-1000 DPI)
- **Smart File Management** with preference persistence and automatic cleanup



### Why EmailFlow?

Traditional email clients require multiple manual steps for batch operations. EmailFlow reduces this to just a few clicks:

1. **Select recipients** from saved contacts (no retyping emails)
2. **Choose files** via folder path or file browser
3. **Optionally convert PDFs** to high-resolution images with your specified DPI
4. **Send with auto-generated or custom subject lines** (date-based or manual)
5. **Automatically clean up files** after sending (optional)


---


## ✨ Key Features

### Email Automation
- **Multi-recipient Management**: Save and manage multiple email addresses
- **SMTP Integration**: Direct email sending via Gmail SMTP (587)
- **Credential Security**: Optional password encryption and on-screen hiding
- **Smart Subject Lines**: Auto-populate with current date (DD-MMM-YYYY format) or use custom subjects
- **Attachment Handling**: Automatically attach files or converted images

### PDF Processing
- **High-Quality Conversion**: Convert PDFs to JPEG images with customizable DPI (10-1000, default: 300)
- **Batch Processing**: Handle multiple PDFs simultaneously with progress tracking
- **Standalone Conversion**: Convert without sending emails via "SAVE IMAGE" feature
- **Multi-threaded Processing**: Background conversion for smooth UI performance

### File Management
- **Dual Selection Modes**: 
  - Browse individual files with native file picker
  - Process entire folders by entering directory path
- **Files Showcase**: Visual preview of selected files before processing
- **Safe Deletion**: Automatically move processed files to recycle bin (not permanent deletion)
- **Buffer Management**: Temporary folder system with automatic cleanup

### User Experience
- **Full Theme Customization**: 
  - Light/Dark mode toggle
  - Custom colors for primary, secondary, menu, and hover elements
  - Persistent theme preferences
- **Settings Persistence**: All preferences saved between sessions in encrypted JSON
- **Internet Validation**: Automatic connectivity check before sending
- **Real-time Feedback**: Progress bars and status notifications
- **Clean Interface**: Modern CustomTkinter UI with logical layout

---

## 📸 Screenshots

<div align="center">

### Main Interface - Light Mode
<img width="1132" height="722" alt="Home Page" src="https://github.com/user-attachments/assets/0d2a0bc5-359a-4fa1-b19f-f86ad3e4bea6" />

*Intuitive main interface with file showcase sidebar*

### Dark Theme
<img width="1132" height="722" alt="Dark Home Page" src="https://github.com/user-attachments/assets/e3d15499-9b2c-428f-bf2a-d492981e450c" />

*Comfortable dark theme for extended use*

### Advanced Customization
<img width="1133" height="724" alt="Choose multiple color customization of ui,buttons,hover,theme,menu" src="https://github.com/user-attachments/assets/75ff7254-51b1-48ab-ab39-cf5431a1ce97" />
<img width="1132" height="722" alt="Cutomized color of UI" src="https://github.com/user-attachments/assets/564845b3-dbbd-4a75-9830-0eb4fe9022a9" />

*Comprehensive color customization for all UI elements*

### Settings Panel
<img width="1132" height="722" alt="Settings Menu" src="https://github.com/user-attachments/assets/8773d7a6-80f3-4711-bd9d-88c77252758a" />

*DPI configuration and application management*


</div>

---

## 🚀 Installation

### Method 1: Windows Executable (Recommended)

**Requirements**: Windows 10 or later

1. Visit the [Releases page](https://github.com/Utkarsh-X/EmailFlow/releases)
2. Download the latest `EmailFlow.zip`
3. Extract to your preferred location
4. Run `EmailFlow.exe`

**No Python installation required!**

### Method 2: Run from Source

**Requirements**: 
- Python 3.8 or higher
- pip package manager
- Poppler (for PDF conversion)

#### Step 1: Clone Repository
```bash
git clone https://github.com/Utkarsh-X/EmailFlow.git
cd EmailFlow
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
```
customtkinter
CTkMessagebox
Pillow
pdf2image
tqdm
requests
send2trash
```

#### Step 3: Install Poppler

**Windows:**
1. Download from [poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases/)
2. Extract and add `bin` folder to system PATH

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

#### Step 4: Run Application
```bash
python EmailFlow.py
```

---

## 🚀 Quick Start Guide

### First Time Setup

1. **Launch Application**
   ```
   Run EmailFlow.exe or python EmailFlow.py
   ```

2. **Configure Sender Credentials**
   - Click "Enter Sender Email" → Enter your Gmail address
   - Click "Enter your Password" → Enter your Gmail App Password
   
   > **Important**: For Gmail, you must use an [App Password](https://support.google.com/accounts/answer/185833), not your regular password. Enable 2-factor authentication first, then generate an app password.

3. **Add Recipients**
   - Click "Add User" button
   - Enter recipient email address
   - Repeat for multiple recipients
   - Select from dropdown when sending

4. **Configure Preferences** (Optional)
   - Open Settings menu (☰ icon)
   - Set default DPI for image conversion
   - Choose theme colors
   - Enable/disable password hiding

### Sending Your First Email

1. **Select Recipient**: Choose from dropdown or add new
2. **Choose Subject**: 
   - Toggle "Subject as Date" for automatic date subject
   - OR enter custom subject in "Enter Email Subject" field
3. **Select Files**:
   - **Option A**: Click "Browse Files" to pick individual files
   - **Option B**: Enter folder path and click "SHOW FILES"
4. **Optional - Convert PDFs**: Toggle "Convert to Image" if sending PDFs as images
5. **Send**: Click "SEND EMAIL" button
6. **Wait for confirmation**: "Uploaded successfully!" message appears

---

## 📖 Detailed Usage

### Email Recipient Management

**Adding Recipients:**
```
1. Click "Add User" button
2. Enter email in dialog box
3. Email saved to dropdown automatically
```

**Removing Recipients:**
```
1. Select email from dropdown
2. Click "Delete User" button
3. Confirm deletion
```

**Tip**: All recipients persist between sessions in `data.json`

### File Selection Modes

#### Mode 1: Browse Files (Individual Selection)
- Click segmented button → "Browse Files"
- Use native file picker to select multiple files
- Preview appears in "Files Showcase" sidebar
- Supports all file types

#### Mode 2: Set Address (Folder Processing Automation)
- Click segmented button → "Set Address" (default)
- Copy the folder path from your deafault File Explorer
- Paste complete folder path in text field
- Click "SHOW FILES" to load all files from folder
- All files in folder will be processed

**Example path formats:**
```
Windows: C:\Users\YourName\Documents\Files
Linux: /home/username/documents/files
macOS: /Users/username/Documents/Files
```

### PDF Conversion Settings

**Accessing DPI Settings:**
```
1. Click menu button (☰)
2. Select "Settings"
3. Find "Set DPI for generated images" section
4. Enter value between 10-1000 (default: 300)
```

**DPI Guidelines:**
| DPI | Use Case | File Size |
|-----|----------|-----------|
| 100-150 | Quick preview, screen viewing | Small |
| 200-300 | Standard documents, printing | Medium |
| 400-600 | High-quality prints, archival | Large |
| 700-1000 | Professional printing, detailed graphics | Very Large |

**Converting Without Sending:**
```
1. Select files/folder
2. Toggle "Convert to Image" ON
3. Click "SAVE IMAGE" button (not SEND EMAIL)
4. Choose destination folder
5. Converted images saved to selected location
```

### Theme Customization

**Changing Theme Mode:**
- Click sun/moon icon (top-right) to toggle light/dark mode

**Custom Colors:**
```
1. Click menu (☰) → "Change Theme"
2. Choose color category:
   - Primary Color: Main buttons and switches
   - Secondary Color: Action buttons (SEND, SAVE)
   - Menu Color: Sidebar background
   - Hover Color: Button hover effects
3. Select color from picker
4. Changes apply immediately
```

**Resetting to Defaults:**
```
Settings → "Default Color" button → Restart application
```

### Advanced Options

**Switch Controls:**

| Switch | Function | Default |
|--------|----------|---------|
| Add Subject | Enable/disable subject field | ON |
| Subject as Date | Auto-populate subject with current date | ON |
| Convert to Image | Enable PDF → Image conversion | OFF |
| Delete files after email | Move files to recycle bin after successful send | ON |
| Always hide password | Mask password with asterisks on main screen | OFF |

**Background Processing:**
- PDF conversion runs in separate thread
- Progress bar shows conversion status
- UI remains responsive during operations

---

## ⚙️ Configuration

### data.json Structure

EmailFlow automatically creates and manages `data.json` in the application directory:

```json
{
    "mode": "light",
    "var4dpi": "300",
    "v2": "encrypted_password_string",
    "v3": "sender@example.com",
    "primary_color": "#1f6aa5",
    "secondary_color": "#144870",
    "menu_color": "#2d2d2d",
    "hover_color": "#333333",
    "switch_v_pass1": "off",
    "list1": [
        "recipient1@example.com",
        "recipient2@example.com"
    ],
    "switch_v_date1": "on",
    "switch_v_sub1": "on",
    "switch_v_img1": "off",
    "switch_v_del1": "on",
    "addre1": "C:\\Users\\Name\\Documents\\LastUsedFolder",
    "recname1": "recipient1@example.com"
}
```

### Configuration Keys Explained

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `mode` | string | UI theme (light/dark) | "light" |
| `var4dpi` | string | Image conversion DPI | "300" |
| `v2` | string | Encrypted sender password | "" |
| `v3` | string | Sender email address | "" |
| `primary_color` | string | Main UI color (hex) | "" |
| `secondary_color` | string | Action button color (hex) | "" |
| `menu_color` | string | Menu background color (hex) | "" |
| `hover_color` | string | Hover effect color (hex) | "" |
| `switch_v_pass1` | string | Password hiding toggle (on/off) | "off" |
| `list1` | array | Saved recipient emails | [] |
| `switch_v_date1` | string | Date subject toggle (on/off) | "on" |
| `switch_v_sub1` | string | Subject field toggle (on/off) | "on" |
| `switch_v_img1` | string | PDF conversion toggle (on/off) | "off" |
| `switch_v_del1` | string | Auto-delete toggle (on/off) | "on" |
| `addre1` | string | Last used folder path | "" |
| `recname1` | string | Last selected recipient | "" |



### Manual Configuration

While not recommended, you can manually edit `data.json`:

1. Close EmailFlow completely
2. Edit `data.json` with text editor
3. Ensure JSON syntax is valid
4. Restart application

**Resetting Configuration:**
```
Settings → "Reset Application" button → Restart
```
This deletes `data.json` and restores all defaults.

---

## 🛠️ Technical Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Core language (100% Python codebase) |
| **CustomTkinter** | 5.0+ | Modern Tkinter-based UI framework |
| **CTkMessagebox** | 2.5+ | Enhanced dialog boxes and notifications |
| **Pillow (PIL)** | 9.0+ | Image processing and manipulation |
| **pdf2image** | 1.16+ | PDF to image conversion via Poppler |
| **Poppler** | Latest | PDF rendering engine |
| **smtplib** | Standard lib | SMTP email protocol implementation |
| **tqdm** | 4.65+ | Progress bar visualization |
| **requests** | 2.28+ | HTTP requests for connectivity checks |
| **send2trash** | 1.8+ | Safe file deletion (recycle bin) |

### Architecture Highlights

- **MVC-inspired Structure**: Separation between UI (EmailFlow.py) and component logic (advmail.py)
- **Multi-threading**: Background processing for PDF conversion and email sending
- **Event-driven UI**: Tkinter event loop with callback functions
- **State Persistence**: JSON-based configuration with automatic save/load
- **Graceful Degradation**: Continues operation even if optional features fail

---

## 📁 Project Architecture

```
EmailFlow/
│
├── assets/                          # Static resources
│   ├── clicktodark.png             # Dark mode toggle icon (21x21)
│   ├── clicktolight.png            # Light mode toggle icon (21x21)
│   ├── emailB.ico                  # Application icon (light)
│   ├── emailL.ico                  # Application icon (dark)
│   └── emailFlow_banner.png        # Banner image for README
│
├── screenshots/                     # Documentation screenshots
│   ├── Home Page.png
│   ├── Dark Home Page.png
│   ├── Settings Menu.png
│   ├── About the software section.png
│   └── Choose multiple color customization....png
│
├── EmailFlow.py                     # Main application GUI
├── advmail.py                       # Backend logic module 
├── version.py                       # Version tracking
├── requirements.txt                 # Python dependencies
├── data.json                        # User configuration (auto-generated)
│
├── LICENSE                          # MIT License
└── README.md                        # This file
```

### Module Breakdown

#### EmailFlow.py (Frontend)
**Responsibilities:**
- Complete UI implementation using CustomTkinter
- User input handling and validation
- Theme management and customization
- Settings persistence (save/load from JSON)
- Integration with backend functions

**Key Components:**
- Frame-based layout system
- Switch toggles for feature control
- Segmented buttons for mode selection
- Scrollable file showcase sidebar
- Color picker dialogs
- Modal dialogs for input

#### advmail.py (Backend)
**Responsibilities:**
- SMTP email transmission
- PDF to image conversion pipeline
- File system operations (list, copy, delete)
- Internet connectivity verification
- Credential validation
- Temporary folder management


### Data Flow

```
User Input (EmailFlow.py)
    ↓
Validation & Processing (EmailFlow.py)
    ↓
Backend Function Calls (advmail.py)
    ↓
SMTP Server / File System
    ↓
Status Notifications (EmailFlow.py)
    ↓
Configuration Save (data.json)
```

---

## 🤝 Contributing

Contributions are welcome and appreciated! Whether you're fixing bugs, adding features, or improving documentation, your help makes EmailFlow better.

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/EmailFlow.git
   cd EmailFlow
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install Development Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Contribution Guidelines

**Code Standards:**
- Follow PEP 8 style guide
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and modular
- Maintain existing code structure

**Testing Requirements:**
- Test on Windows (primary platform)
- Verify UI changes in both light/dark themes
- Test with various file types and sizes
- Ensure backward compatibility with existing data.json

**Pull Request Process:**
1. Update README if adding features
2. Test thoroughly across different scenarios
3. Provide clear description of changes
4. Reference any related issues
5. Wait for code review and address feedback

### Priority Areas for Contribution

**High Priority:**
- [ ] Multiple SMTP provider support (Gmail, Outlook, Yahoo, custom servers)
- [ ] Enhanced encryption for stored passwords
- [ ] Comprehensive error logging system
- [ ] Unit test suite

**Medium Priority:**
- [ ] Internationalization (i18n) support
- [ ] Export email history to CSV/Excel
- [ ] Scheduled/delayed email sending
- [ ] Email templates system

**Nice to Have:**
- [ ] macOS and Linux testing/optimization
- [ ] Drag-and-drop file selection
- [ ] Email signature support
- [ ] Attachment size warnings
- [ ] Dark mode refinements

### Reporting Bugs

**Before Submitting:**
1. Check existing [Issues](https://github.com/Utkarsh-X/EmailFlow/issues)
2. Verify you're using the latest version
3. Try reproducing with default settings

**Include in Report:**
- EmailFlow version
- Operating system and version
- Python version (if running from source)
- Steps to reproduce
- Expected vs actual behavior
- Screenshots/error messages
- data.json contents (remove sensitive info)

---


## 🔧 Troubleshooting

### Common Issues

#### "Invalid credentials" Error

**Cause**: Incorrect email/password or Gmail security settings

**Solutions:**
1. Verify email address is correct
2. For Gmail users:
   - Enable 2-factor authentication
   - Generate App Password at https://myaccount.google.com/apppasswords
   - Use App Password instead of regular password
3. Check internet connection
4. Verify SMTP server is accessible

#### PDF Conversion Fails

**Error**: "Poppler not found" or conversion hangs

**Solutions:**
1. Verify Poppler is installed:
   ```bash
   # Windows: Check PATH includes poppler/bin
   # Linux: dpkg -l | grep poppler
   # Mac: brew list poppler
   ```
2. Reinstall Poppler following installation guide
3. Check PDF isn't corrupted (try opening in Adobe Reader)
4. Reduce DPI if file is very large

#### Files Not Appearing in Showcase

**Cause**: Invalid folder path or permission issues

**Solutions:**
1. Verify folder path is complete and correct
2. Use forward slashes (/) or escaped backslashes (\\) on Windows
3. Check folder isn't empty
4. Ensure you have read permissions for folder
5. Click "SHOW FILES" button after entering path

#### Application Won't Start

**Solutions:**
1. Check Python version: `python --version` (must be 3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
3. Delete data.json and restart
4. Check for conflicting tkinter installations
5. Run from command line to see error messages

#### UI Elements Not Displaying Correctly

**Solutions:**
1. Update CustomTkinter: `pip install --upgrade customtkinter`
2. Try resetting custom colors (Settings → Default Color)
3. Toggle between light/dark mode
4. Restart application
5. Delete data.json and reconfigure

### Getting Help

1. **Documentation**: Review this README thoroughly
2. **Issues**: Search [GitHub Issues](https://github.com/Utkarsh-X/EmailFlow/issues)
3. **New Issue**: Open detailed bug report with system info
4. **Discussions**: For questions and feature requests

---

## Contact & Support

**Developer**: Utkarsh-X

**Links:**
- GitHub Profile: [@Utkarsh-X](https://github.com/Utkarsh-X)
- Project Repository: [EmailFlow](https://github.com/Utkarsh-X/EmailFlow)
- Issue Tracker: [Issues](https://github.com/Utkarsh-X/EmailFlow/issues)
- Latest Release: [Releases](https://github.com/Utkarsh-X/EmailFlow/releases)

### Support Channels

**For Bugs:**
1. Check [existing issues](https://github.com/Utkarsh-X/EmailFlow/issues)
2. Open new issue with detailed information
3. Include screenshots and error logs

**For Feature Requests:**
1. Open GitHub issue with "Feature Request" label
2. Describe use case and expected behavior
3. Explain why feature would be valuable

**For General Questions:**
- Open GitHub Discussion
- Check README and documentation first

## 📊 Version History

| Version     | Date      | Changes                                                   |
|-------------|-----------|------------------------------------------------------------|
| **v1.5.01** | Sep 2025  | Bug fixes, UI improvements, enhanced security              |
| **v1.4.22** | Aug 2025  | Performance optimizations, stability improvements          |
| **v1.3.x**  | 2024      | Feature additions and refinements *(Not available online)* |
| **v1.0.x**  | 2024      | Initial releases *(Not available online)*                  |



See [full release notes](https://github.com/Utkarsh-X/EmailFlow/releases) for detailed changelog.

---

## 🌟 Show Your Support

If EmailFlow helps streamline your workflow, please consider:

- ⭐ **Star this repository** - Helps others discover the project
- 🐛 **Report bugs** - Improves stability for everyone
- 💡 **Suggest features** - Shapes future development
- 🤝 **Contribute code** - Makes EmailFlow better
- 📢 **Share with others** - Grows the community

---

<div align="center">

**Built with Python • Designed for Simplicity • Open Source Forever**

Made by [Utkarsh-X](https://github.com/Utkarsh-X)

[⬆ Back to Top](#emailflow)

</div>
