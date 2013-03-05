# !/bin/bash

#
#   Copyright 2009 IP Info DB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

# author: Simone Tripodi (simone.tripodi)
# version: $Id: install-ipinfo-db.sh 2 2009-07-04 14:28:38Z simone.tripodi $

if ! [ -n "$1" ] || ! [ -n "$2" ]; then
    echo "Usage: sh install-ipinfo-db.sh [mysql-username] [mysql-password]";
    exit 1;
fi

wget http://mirrors.portafixe.com/ipinfodb/ip_database/current/ipinfodb_mul_table_full.sql.bz2
bunzip2 ipinfodb_mul_table_full.sql.bz2
mysql --user $1 --password=$2 ipinfo < ipinfodb_mul_table_full.sql
rm ipinfodb_mul_table_full.sql
