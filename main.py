
#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.





from sipproxy import *


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    #ipaddress = socket.gethostbyname(hostname)
    #if ipaddress == "127.0.0.1":
    #    ipaddress = sys.argv[1]
    ipaddress = sys.argv[1]
    logging.info(ipaddress)
    set_recordRoute("Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT))
    setTopVia("Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT))
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    server.serve_forever()
