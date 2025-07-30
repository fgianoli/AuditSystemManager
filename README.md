# 🔍 Audit System Manager - QGIS Plugin

[![QGIS](https://img.shields.io/badge/QGIS-3.x+-brightgreen.svg)](https://qgis.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-9.5+-blue.svg)](https://postgresql.org)
[![Python](https://img.shields.io/badge/Python-3.6+-yellow.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-GPL%20v2-orange.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-green.svg)]()

A comprehensive QGIS plugin for PostgreSQL database audit monitoring, versioning, and rollback operations. Provides real-time change tracking, data versioning, and recovery capabilities for spatial and non-spatial databases.

## 📸 Screenshots

| Real-Time Monitoring | Version Comparison | Rollback Operations |
|:---:|:---:|:---:|
| ![Monitoring](docs/images/monitoring.png) | ![Versioning](docs/images/versioning.png) | ![Rollback](docs/images/rollback.png) |
| *Live change tracking with smart filtering* | *Side-by-side version comparison* | *Single and batch rollback operations* |

## ✨ Key Features

### 🎯 **Real-Time Monitoring**
- **Live Change Tracking**: Monitor INSERT, UPDATE, DELETE operations as they happen
- **Smart Filtering**: Advanced filters by user, schema, table, time period, and operation type  
- **Intelligent Search**: Natural language search with syntax like `user:john`, `table:buildings`, `today`
- **Visual Indicators**: Color-coded operations and enhanced record ID detection
- **Auto-Refresh**: Configurable automatic data refresh intervals

### 📦 **Data Versioning**
- **Complete History**: Track all changes with automatic version numbering
- **Field-by-Field Diff**: Visual comparison between versions with highlighted changes
- **Record-Specific View**: Filter complete history by specific record IDs
- **Change Summaries**: Human-readable summaries of modifications
- **Export Capabilities**: Export version history to CSV with metadata

### ⏪ **Rollback & Recovery**
- **Precision Rollback**: Restore individual records to any previous version
- **User Change Undo**: Bulk undo all changes made by specific users within time windows
- **Batch Operations**: Mass rollback operations across multiple tables and schemas
- **Dry Run Mode**: Preview rollback operations before execution
- **Rollback Audit**: Complete logging of all recovery operations

### 🛠 **System Management**
- **One-Click Setup**: Automated audit system installation with comprehensive SQL scripts
- **Schema Configuration**: Granular control over which schemas and tables to monitor
- **Connection Management**: Secure database connection handling with encrypted credential storage
- **Performance Monitoring**: Real-time system metrics, user activity, and storage analytics
- **Health Dashboard**: Monitor system performance and audit log growth

## 🔧 Technical Requirements

### **Software Dependencies**
- **QGIS**: Version 3.x or higher
- **PostgreSQL**: Version 9.5+ with JSON support
- **Python**: 3.6+ (included with QGIS)

### **Python Libraries**
```bash
pip install psycopg2-binary  # PostgreSQL adapter
```

### **Database Permissions**
- **CREATE** privileges for initial system setup
- **TRIGGER** privileges for audit installation
- **INSERT/SELECT** on audit tables (automatically configured)

### **Supported PostgreSQL Features**
- JSON/JSONB data types
- PL/pgSQL procedural language
- Trigger functions
- System catalogs access

## 📥 Installation

### **Method 1: QGIS Plugin Manager (Recommended)**
1. Open QGIS
2. Go to `Plugins` → `Manage and Install Plugins`
3. Search for "Audit System Manager"
4. Click `Install Plugin`

### **Method 2: Manual Installation**
1. Download the latest release from [Releases](../../releases)
2. Extract to your QGIS plugins directory:
   - **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin in `Plugins` → `Manage and Install Plugins` → `Installed`

### **Method 3: Development Version**
```bash
git clone https://github.com/yourusername/audit-system-manager.git
cd audit-system-manager
# Copy to QGIS plugins directory
cp -r . ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/audit_system_manager/
```

## ⚙️ Configuration

### **1. Database Connection Setup**
1. Launch the plugin from the toolbar or `Plugins` menu
2. Click `Change Connection` in the Configuration tab
3. Enter your PostgreSQL connection details:
   ```
   Host: localhost (or your server IP)
   Port: 5432
   Database: your_database_name
   Username: your_username
   Password: your_password
   ```
4. Click `Test Connection` to verify
5. Save the configuration

### **2. Audit System Installation**
1. Go to Configuration tab → `Setup Audit System`
2. Click `Install Audit System` (requires CREATE privileges)
3. The installer will create:
   - `logging` schema with audit tables
   - Trigger functions for change tracking
   - Versioning and rollback functions
   - Performance indexes
   - Security permissions

### **3. Schema Selection**
1. In the setup dialog, go to `Configure Monitoring` tab
2. Select schemas to monitor from the available list
3. Add individual tables if needed
4. Click `Apply Configuration`
5. Triggers will be automatically created on selected tables

## 🚀 Usage Guide

### **Real-Time Monitoring**
```
1. Open the Monitoring tab
2. Use quick action buttons for common tasks:
   - 🔄 Refresh: Update data manually
   - 📅 Today: Filter to today's changes only
   - 👤 My Changes: Show only your modifications
   - ⚡ Last 50: Display most recent changes
3. Use Smart Search for advanced filtering:
   - "user:john table:buildings today"
   - "insert delete schema:gis"
4. Double-click Record IDs to copy to clipboard
5. Right-click rows for context menu options
```

### **Version Analysis**
```
1. Go to Versioning tab
2. Select schema and table
3. Optionally filter by specific Record ID
4. Click "Load History"
5. Select multiple versions to compare
6. Use "Details" button for complete change information
7. Export history to CSV for external analysis
```

### **Data Recovery**
```
Single Record Rollback:
1. Go to Rollback tab → Single Record
2. Enter schema, table, version number
3. Provide rollback reason
4. Execute rollback

User Change Undo:
1. Go to Rollback tab → User Changes  
2. Select user and time window
3. Click "Test (Dry Run)" first
4. Review changes to be undone
5. Execute if satisfied
```

## 🏗 Architecture

### **Database Components**
```sql
logging/
├── t_history              # Main audit table
├── t_rollback_history     # Rollback operations log
├── notify_with_versioning() # Trigger function
├── rollback_record_to_version() # Recovery function
├── undo_user_changes()    # Bulk undo function
└── v_recent_changes       # Convenience view
```

### **Trigger System**
- **Automatic**: Triggers created on monitored tables
- **Comprehensive**: Captures INSERT, UPDATE, DELETE operations
- **Metadata**: Records user, timestamp, IP, application name
- **JSON Storage**: Before/after states stored as JSON
- **Versioning**: Automatic version number assignment

### **Plugin Architecture**
```
AuditSystemManager/
├── AuditSystemManager.py    # Main plugin class
├── DatabaseConfigDialog     # Connection management  
├── AuditSetupDialog        # System installation
├── AuditDialog             # Main interface
├── HelpDialog              # Documentation
└── Utility Functions       # Helper methods
```

## 📊 Database Schema

### **Main Audit Table**
```sql
CREATE TABLE logging.t_history (
    id                 serial PRIMARY KEY,
    tstamp             timestamp DEFAULT now(),
    epoc               float,
    schemaname         text,
    tabname            text,
    operation          text,
    who                text DEFAULT current_user,
    new_val            json,    -- After state
    old_val            json,    -- Before state
    version_number     integer,
    is_current         boolean DEFAULT true,
    change_reason      text,
    user_ip            text,
    application_name   text
);
```

### **Performance Indexes**
```sql
-- Optimized for common query patterns
CREATE INDEX idx_t_history_tstamp ON logging.t_history (tstamp);
CREATE INDEX idx_t_history_schema_table ON logging.t_history (schemaname, tabname);
CREATE INDEX idx_t_history_user ON logging.t_history (who);
CREATE INDEX idx_t_history_operation ON logging.t_history (operation);
CREATE INDEX idx_t_history_current ON logging.t_history (schemaname, tabname, is_current) 
WHERE is_current = true;
```

## 🔐 Security Features

### **Access Control**
- **SECURITY DEFINER**: Functions run with elevated privileges
- **Controlled Access**: Users don't need direct table privileges
- **Audit Trail**: Complete record of all access and modifications
- **IP Tracking**: Source IP address logging for security

### **Data Protection**
- **Encrypted Storage**: Connection credentials encrypted in QGIS settings
- **Audit Integrity**: Audit records cannot be modified by regular users
- **Change Validation**: Rollback operations require explicit confirmation
- **Rollback Logging**: All recovery operations are themselves audited

## 🧪 Testing

### **Manual Testing**
1. Create test tables with various data types
2. Perform INSERT, UPDATE, DELETE operations
3. Verify audit records are created correctly
4. Test rollback functionality
5. Validate user permissions and security

### **Performance Testing**
```sql
-- Test with high-volume changes
INSERT INTO test_table SELECT generate_series(1,10000), 'test_data';
UPDATE test_table SET data = 'modified' WHERE id < 5000;
DELETE FROM test_table WHERE id > 8000;

-- Verify audit performance
SELECT COUNT(*) FROM logging.t_history WHERE tabname = 'test_table';
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### **Development Setup**
```bash
git clone https://github.com/yourusername/audit-system-manager.git
cd audit-system-manager
git checkout -b feature/your-feature-name
```

### **Code Standards**
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions
- Include error handling
- Test changes thoroughly

### **Pull Request Process**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

### **Bug Reports**
Please use the [Issue Tracker](../../issues) and include:
- QGIS version
- PostgreSQL version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs

## 📚 Documentation

### **Additional Resources**
- [User Manual](docs/user-manual.md) - Comprehensive usage guide
- [API Documentation](docs/api.md) - Function reference
- [FAQ](docs/faq.md) - Common questions and solutions
- [Troubleshooting](docs/troubleshooting.md) - Problem resolution
- [Examples](docs/examples/) - Sample configurations and use cases

### **Video Tutorials**
- [Installation Guide](https://youtube.com/watch?v=example1)
- [Basic Configuration](https://youtube.com/watch?v=example2)
- [Advanced Features](https://youtube.com/watch?v=example3)

## 🌐 Internationalization

Currently supported languages:
- **English** (default)
- **Italian** (native)

To add a new language:
1. Create translation files in `i18n/` directory
2. Use Qt Linguist for translation
3. Submit a pull request

## 📈 Roadmap

### **Version 2.0 (Planned)**
- [ ] Real-time notifications
- [ ] Advanced reporting dashboard
- [ ] REST API for external access
- [ ] Multi-database support
- [ ] Performance analytics
- [ ] Automated backup integration

### **Future Enhancements**
- [ ] Web-based interface
- [ ] Machine learning anomaly detection
- [ ] Integration with other QGIS plugins
- [ ] Cloud database support
- [ ] Mobile companion app

## 📄 License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.

### **Third-Party Licenses**
- Qt Framework: LGPL
- PostgreSQL: PostgreSQL License
- QGIS: GPL v2
- psycopg2: LGPL

## 👥 Authors

- **Federico Gianoli** - *Initial work* - [gianoli.federico@gmail.com](mailto:gianoli.federico@gmail.com)

See also the list of [contributors](../../contributors) who participated in this project.

## 🙏 Acknowledgments

- QGIS Development Team for the excellent framework
- PostgreSQL Community for robust database features
- Italian GIS Community for testing and feedback
- Open Source contributors who made this possible

## 📞 Support

### **Getting Help**
- 📖 Check the [Documentation](docs/)
- 🐛 Report bugs in [Issues](../../issues)
- 💬 Ask questions in [Discussions](../../discussions)
- 📧 Email: [gianoli.federico@gmail.com](mailto:gianoli.federico@gmail.com)

### **Commercial Support**
Professional support, customization, and training available upon request.

---

<div align="center">

**⭐ If this plugin helps you, please consider giving it a star!**

[Report Bug](../../issues) · [Request Feature](../../issues) · [Documentation](docs/) · [Examples](examples/)

</div>
