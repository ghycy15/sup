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
package com.ipinfodb.rest.setup;

import com.asemantics.commons.injectlet.AbstractGuiceServletContextListener;
import com.google.inject.Binder;
import com.google.inject.Module;
import com.ibatis.sqlmap.client.SqlMapClient;
import com.ipinfodb.rest.dao.SqlMapProvider;

/**
 * 
 * @author Simone Tripodi
 * @version $Id: IpLocationContextListener.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
public final class IpLocationContextListener extends AbstractGuiceServletContextListener {

    public IpLocationContextListener() {
        super(new Module() {
            public void configure(Binder binder) {
                binder.bind(SqlMapClient.class).toProvider(new SqlMapProvider("com/ipinfodb/rest/dao/sqlmap-config.xml"));
            }
        });
    }

}
