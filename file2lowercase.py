#!/usr/bin/env python
'''
Copyright (c) 2015-Present Juan Espinoza. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

	1. Redistributions of source code must retain the above copyright notice,
	this list of conditions and the following disclaimer.
	2. Redistributions in binary form must reproduce the above copyright notice,
	this list of conditions and the following disclaimer in the documentation
	and/or other materials provided with the distribution.
	3. Neither the name of the copyright holder nor the names of its
	contributors may be used to endorse or promote products derived from this
	software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import click
import os

@click.command()
@click.argument('filename', nargs=-1, required=True)
@click.option("-v", is_flag=True, help="Enable verbose mode.")
@click.option("-f", is_flag=True, help="Force overwrite.")

def lower_fname(filename, v, f):
        """Rename the given argument[s] to lowercase."""
        for _ in filename:
                # convert tuple element (unicode) to string
                _ = str(_)
                # Ensure file exists before comitting any changes
                if os.path.isfile(_):
                    # Show files being modified, if verbose mode is enabled.
                    if v:
                        print 'Renaming %s => %s' % (_, str.lower(_))
                    # Prompt user to confirm overwrite - if similar lowercase
                    # file exists.
                    if os.path.isfile(str.lower(_)):
                        # Force overwrite if -f flag is True
                        if f:
                            print "WARNING: File %s exists - overwritting."                            % str.lower(_)
                            os.rename(_, str.lower(_))
                        else:
                            # Prompt user to confirm overwrite - if similar
                            # named lowercase file exists.
                            print "WARNING: File %s exists." % str.lower(_)
                            o = raw_input("Overwrite? y/N: ")
                            if (o == 'y') or ( o =='Y'):
                                os.rename(_, str.lower(_))
                    else:
                        os.rename(_, str.lower(_))
                else:
                    exit('ERROR: File[s] specified could not be found.')

if __name__ == '__main__':
        lower_fname()
