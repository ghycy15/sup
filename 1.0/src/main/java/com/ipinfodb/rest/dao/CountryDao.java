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
import java.util.List;

import com.ipinfodb.rest.domain.Country;
import com.ipinfodb.rest.domain.IpRange;

/**
 * 
 * @author Simone Tripodi
 * @version $Id: CountryDao.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
public final class CountryDao extends AbstractDao {

    private static final String SELECT_ALL_COUNTRY_LIST = "country.selectAllCountries";

    private static final String SELECT_IP_RANGES_COUNTRY = "country.selectIpRangesByCountry";

    @SuppressWarnings("unchecked")
    public List<Country> selectAllCountries() throws DaoException {
        try {
            return this.getSqlMapClient().queryForList(SELECT_ALL_COUNTRY_LIST);
        } catch (SQLException e) {
            throw new DaoException("An error occurred while retrieving the complete Country list", e);
        }
    }

    @SuppressWarnings("unchecked")
    public List<IpRange> selectIpRangesByCountry(final List<String> countryCode) throws DaoException {
        try {
            return this.getSqlMapClient().queryForList(SELECT_IP_RANGES_COUNTRY, countryCode);
        } catch (SQLException e) {
            throw new DaoException("An error occurred while retrieving the ip range by country '"
                    + countryCode
                    + "'", e);
        }
    }

}
