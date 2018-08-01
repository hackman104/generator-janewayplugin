'use strict';
const Generator = require('yeoman-generator');
const chalk = require('chalk');
const yosay = require('yosay');
const path = require('path');
const basedir = path.basename(process.cwd());

module.exports = class extends Generator {
  constructor(args, opts) {
    super(args, opts);

    this.argument('appname', { type: String, required: false });
  }

  prompting() {
    // Have Yeoman greet the user.
    this.log(yosay(`Welcome to the ${chalk.red('generator-janewayplugin')} generator!.`));

    const prompts = [
      {
        type: 'input',
        name: 'name',
        message: 'Your plugin name',
        default: this.options.appname ? this.options.appname : basedir
      },
      {
        type: 'input',
        name: 'description',
        message: 'Description of your plugin',
        default: 'N/A'
      },
      {
        type: 'input',
        name: 'author',
        message: 'Plugin author',
        store: true
      },
      {
        type: 'input',
        name: 'version',
        message: 'Version number',
        default: '1.0'
      },
      {
        type: 'input',
        name: 'shortName',
        message: 'Short, one-word name for your plugin',
        validate: str => {
          return str.split(' ').length === 1 ? true : 'Your shortname must be one word long';
        }
      },
      {
        type: 'confirm',
        name: 'workflow',
        message: 'Is this a workflow plugin?'
      }
    ];

    return this.prompt(prompts).then(props => {
      // To access props later use this.props.someAnswer;
      this.props = props;
    });
  }

  writing() {
    this.fs.copyTpl(this.templatePath('README.md'), this.destinationPath('README.md'), {
      pluginName: this.props.name,
      description: this.props.description
    });

    this.fs.copyTpl(
      this.templatePath('plugin_settings.py'),
      this.destinationPath('plugin_settings.py'),
      {
        pluginName: this.props.name,
        description: this.props.description,
        author: this.props.author,
        version: this.props.version,
        shortName: this.props.shortName,
        managerUrl: this.props.shortName + '_index'
      }
    );

    this.fs.copyTpl(this.templatePath('hooks.py'), this.destinationPath('hooks.py'), {
      dirName: basedir,
      shortName: this.props.shortName
    });

    this.fs.copyTpl(this.templatePath('__init__.py'), this.destinationPath('__init__.py'), {});

    this.fs.copyTpl(this.templatePath('urls.py'), this.destinationPath('urls.py'), {
      dirName: basedir,
      managerUrl: this.props.shortName + '_index'
    });

    this.fs.copyTpl(this.templatePath('views.py'), this.destinationPath('views.py'), {
      dirName: basedir,
      shortName: this.props.shortName,
      managerUrl: this.props.shortName + '_index'
    });

    this.fs.copyTpl(this.templatePath('forms.py'), this.destinationPath('forms.py'), {
      shortName: this.props.shortName
    });

    this.fs.copyTpl(
      this.templatePath('inject.html'),
      this.destinationPath(`templates/${basedir}/inject.html`),
      {}
    );

    this.fs.copyTpl(
      this.templatePath('index.html'),
      this.destinationPath(`templates/${basedir}/index.html`),
      {
        shortName: this.props.shortName,
        pluginName: this.props.name
      }
    );
  }
};
