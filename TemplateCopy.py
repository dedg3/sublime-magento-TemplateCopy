# utf-8

# Copyright (c) 2012 dedg3
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# @author dedg3 | git@dedge.org | twitter.com/dedg3
# @copyright (c) 2012 dedg3
# @link https://github.com/dedg3/sublime-magento-TemplateCopy

import sublime, sublime_plugin, os, shutil

class magentoTemplateCopyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        currentTheme = sublime.active_window().active_view().settings().get('tc_theme')
        magentoEnterprise = sublime.active_window().active_view().settings().get('tc_enterprise')

        def open_targetFile(TARGET):
            if os.path.isfile(TARGET):
                print "Opening file '%s'" % (TARGET)
                self.view.window().open_file(TARGET)
            else:
                print "File does not exist: '%s'" % (TARGET)


        if self.view.file_name().find('frontend') > 0:
            if len(self.view.file_name()) > 0:
                source   = self.view.file_name()
                path     = os.path.split(source)[0]
                filename = os.path.split(source)[1]

                if magentoEnterprise == "true":
                    tmpPath = 'enterprise'
                else:
                    tmpPath = 'base'

                if path.find('enterprise') > 0:
                    sourcePath = path
                    targetPath = path.replace("default",currentTheme)
    

                else:
                    sourcePath = path
                    targetPath =path.replace("base",tmpPath).replace("default",currentTheme)
       
                SOURCE = sourcePath+"/"+filename
                TARGET = targetPath+"/"+filename

                if os.path.isfile(targetPath):
                    open_targetFile(TARGET)
                else:
                    if os.access(targetPath, os.F_OK) == False:
                        os.makedirs(targetPath)
                        shutil.copyfile(SOURCE,TARGET)
                        open_targetFile(TARGET)
                    else:
                        shutil.copyfile(SOURCE,TARGET)
                        open_targetFile(TARGET)


        else:
            sublime.status_message('No Magento Template file!')