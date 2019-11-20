#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Markus Liljedahl
# Copyright (c) 2017 Markus Liljedahl
#
# License: MIT
#

from SublimeLinter.lint import Linter, util

import re


class CfnLint(Linter):
    """Provides an interface to cfn-lint."""

    cmd = ('cfn-lint', '--template', '${file}', '--format', 'parseable')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+):\d+:\d+:((?P<warning>W|I)|(?P<error>E))(?P<code>.{4}):(?P<message>.+)'
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT
    word_re = None

    defaults = {
        'selector': 'source.yaml, source.json',
        'strict': True
    }

    def communicate(self, cmd, code=None):
        """Run an external executable using stdin to pass code and return its output."""
        relfilename = self.filename

        is_cfn = False

        # Check if we're processing a CloudFormation file
        with open(relfilename, 'r', encoding='utf8') as file:
            content = file.read()
            regex = re.compile(r'"?AWSTemplateFormatVersion"?\s*')

            if regex.search(content):
                is_cfn = True

        if is_cfn:
            # Add ignore rules
            ignore_rules = self.settings.get('ignore_rules', [])
            if len(ignore_rules) > 0:

                cmd.append('--ignore-checks')

                for ignore_rule in ignore_rules:
                    cmd.append(ignore_rule)

            # Add apprent rules paths
            append_rules = self.settings.get('append_rules', [])
            if len(append_rules) > 0:

                cmd.append('--append-rules')

                for append_rule in append_rules:
                    cmd.append(append_rule)

            # Add override specification file
            override_spec = self.settings.get('override_spec')
            if override_spec:
                cmd.append('--override-spec')
                cmd.append(override_spec)

            include_checks = self.settings.get('include_checks', [])
            if len(include_checks) > 0:

                cmd.append('--include-checks')

                for include_rule in include_checks:
                    cmd.append(include_rule)

            print(cmd)

            return super().communicate(cmd, code)
