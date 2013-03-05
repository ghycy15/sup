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
package com.ipinfodb.rest.services;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import com.google.inject.Inject;
import com.google.inject.Singleton;
import com.ipinfodb.rest.dao.CountryDao;
import com.ipinfodb.rest.dao.DaoException;
import com.ipinfodb.rest.domain.Country;
import com.ipinfodb.rest.domain.IpRange;
import com.ipinfodb.rest.domain.ServiceError;
import com.sun.jersey.impl.ResponseBuilderImpl;

/**
 * 
 * @author Simone Tripodi
 * @version $Id: CountryService.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
@Singleton
@Path("countries")
public final class CountryService {

    private final Log log = LogFactory.getLog(this.getClass());

    @Inject
    private CountryDao countryDao;

    public void setCountryDao(final CountryDao countryDao) {
        this.countryDao = countryDao;
    }

    @GET
    @Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
    @Path("list")
    public List<Country> getAllCountries() {
        try {
            return this.countryDao.selectAllCountries();
        } catch (DaoException e) {
            String errorMessage = "An internal error occurred while retrieving the complete Country list";
            this.log.error(errorMessage, e);
            ServiceError serviceError = new ServiceError();
            serviceError.setMessage(errorMessage);

            throw new WebApplicationException(new ResponseBuilderImpl()
                    .entity(serviceError)
                    .status(Response.Status.INTERNAL_SERVER_ERROR)
                    .build());
        }
    }

    @GET
    @Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
    @Path("ips")
    public List<IpRange> getIpRangesByCountry(@QueryParam("countryCode") final List<String> countryCode) {
        if (countryCode == null) {
            String errorMessage = "One or more country code has to be specified, use 'countryCode' parameter";
        this.log.warn(errorMessage);
        ServiceError serviceError = new ServiceError();
        serviceError.setMessage(errorMessage);

        throw new WebApplicationException(new ResponseBuilderImpl()
                .entity(serviceError)
                .status(Response.Status.BAD_REQUEST)
                .build());
        }

        List<IpRange> ipRanges = null;

        try {
            ipRanges = this.countryDao.selectIpRangesByCountry(countryCode);
        } catch (DaoException e) {
            String errorMessage = "An error occurred while retrieving the ip range by country "
                    + countryCode;
            this.log.error(errorMessage, e);
            ServiceError serviceError = new ServiceError();
            serviceError.setMessage(errorMessage);

            throw new WebApplicationException(new ResponseBuilderImpl()
                    .entity(serviceError)
                    .status(Response.Status.INTERNAL_SERVER_ERROR)
                    .build());
        }

        if (ipRanges == null || ipRanges.isEmpty()) {
            String errorMessage = "No ip range found for country '"
                    + countryCode
                    + "'";

            if (this.log.isWarnEnabled()) {
                this.log.warn(errorMessage);
            }

            ServiceError serviceError = new ServiceError();
            serviceError.setMessage(errorMessage);

            throw new WebApplicationException(new ResponseBuilderImpl()
                .entity(serviceError)
                .status(Response.Status.NO_CONTENT)
                .build());
        }

        return ipRanges;
    }

}
