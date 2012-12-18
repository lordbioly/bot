from chatterbotapi import ChatterBotFactory, ChatterBotType

"""
    chatterbotapi
    Copyright (C) 2011 pierredavidbelanger@gmail.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.
    
    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.JABBERWACKY)
bot2session = bot2.create_session()


while (1):
    
    s = raw_input()
	
    
    s = bot2session.think(s);
    print 'bot2> ' + s
    
    