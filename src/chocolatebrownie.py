# This file is part of ChocolateBrownie.
#
# ChocolateBrownie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ChocolateBrownie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ChocolateBrownie.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Aleksandar Savkov'

from pygments.style import Style
from pygments.token import Text, Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Punctuation


class ChocolatebrownieStyle(Style):

    styles = {
        Text:                       '#F5E9DC',  # pale orange

        Comment:                    'italic #5A4A54',  # adamantium
        Comment.Multiline:          'italic',  # adamantium
        Comment.Preproc:            'bold',
        Comment.Special:            'bold italic',

        Keyword:                    'bold #713D6E',  # poison jelly

        Operator:                   'bold #700B30',  # raspberry

        Generic:                    '#B81A42',  # poison apple

        Name:                       '#c39873',  # nougat
        Name.Attribute:             '#c39873',  # nougat
        Name.Builtin:               '#713D6E',  # poison jelly
        Name.Builtin.Pseudo:        '#713D6E',  # poison jelly
        Name.Class:                 '#C1B3D4',  # wandering soul
        Name.Exception:             'bold #600000',  # saffron
        Name.Function:              'bold #C1B3D4',  # wandering soul

        Number:                     '#633B1D',  # laura's cooking cream

        String:                     '#7AA7D6',  # love is everything
        String.Backtick:            'italic',
        String.Escape:              '#B14623',  # tricky 4

        Punctuation:                '#ffffff'
    }