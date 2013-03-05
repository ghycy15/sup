/*
 *  Copyright 2009 IP Info DB
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package com.ipinfodb.rest.dao;

import java.sql.SQLException;

import com.google.inject.Singleton;
import com.ipinfodb.rest.domain.Location;

/**
 * 
 * @author Simone Tripodi
 * @version $Id: LocationDao.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
@Singleton
public final class LocationDao extends AbstractDao {

    private static final String SELECT_LOCATION = "location.selectLocationByIp";

    public Location selectLocationByIp(final String ip) throws DaoException {
        try {
            return (Location) this.getSqlMapClient().queryForObject(SELECT_LOCATION, ip);
        } catch (SQLException e) {
            throw new DaoException("An error occurred while retrieving the location for ip '"
                    + ip
                    + "', see nested exception", e);
        }
    }

}
