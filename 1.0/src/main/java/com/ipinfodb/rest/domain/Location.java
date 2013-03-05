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
package com.ipinfodb.rest.domain;

import java.io.Serializable;

/**
 * 
 * @author Simone Tripodi
 * @version $Id: Location.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
public final class Location implements Serializable {

    private static final long serialVersionUID = 1L;

    private String countryCode;

    private String countryName;

    private String regionName;

    private String city;

    private String zipPostalCode;

    private float latitude;

    private float longitude;

    private float gmtOffset;

    private float dstOffset;

    public String getCountryCode() {
        return this.countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getCountryName() {
        return this.countryName;
    }

    public void setCountryName(String countryName) {
        this.countryName = countryName;
    }

    public String getRegionName() {
        return this.regionName;
    }

    public void setRegionName(String regionName) {
        this.regionName = regionName;
    }

    public String getCity() {
        return this.city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getZipPostalCode() {
        return this.zipPostalCode;
    }

    public void setZipPostalCode(String zipPostalCode) {
        this.zipPostalCode = zipPostalCode;
    }

    public float getLatitude() {
        return this.latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }

    public float getLongitude() {
        return this.longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }

    public float getGmtOffset() {
        return this.gmtOffset;
    }

    public void setGmtOffset(float gmtOffset) {
        this.gmtOffset = gmtOffset;
    }

    public float getDstOffset() {
        return this.dstOffset;
    }

    public void setDstOffset(float dstOffset) {
        this.dstOffset = dstOffset;
    }

    @Override
    public String toString() {
        return "(countryCode="
                + this.countryCode
                + ", countryName="
                + this.countryName
                + ", regionName="
                + this.regionName
                + ", city="
                + this.city
                + ", zipPostalCode="
                + this.zipPostalCode
                + ", latitude="
                + this.latitude
                + ", longitude="
                + this.longitude
                + ", gmtOffset="
                + this.gmtOffset
                + ", dstOffset="
                + this.dstOffset
                + ")";
    }

}
