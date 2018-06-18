SublimeLinter-contrib-cloudformation
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-cloudformation.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-cloudformation)


This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [cfn-lint](https://github.com/awslabs/cfn-python-lint). This plugin lints `yaml` and `json` CloudFormation templates.


## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `cfn-lint` is installed on your system.

```
pip install cfn-lint
```

**Note**: This plugin requires cfn-lint 0.2.2 or later.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure `cfn-lint` by adding the following options to the Sublime Linter User Settings:

* ignore_rules: Array of rules that should be ignored when testing the file
* append_rules: Array of paths containing additional rules to be applied
* override_spec: Path the a Specification Override file

Example:

```json
{
  "linters": {
	  "cfnlint": {
	    "ignore_rules": ["W2507", "W2508"],
	    "append_rules": ["/path/to/custom/rules"],
	    "override_spec": "/path/to/override.json"
	  }
	}
}
```

For details about these settings, check the [cfn-lint documentation](https://github.com/awslabs/cfn-python-lint#parameters)
