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
package com.ipinfodb.rest.services.writers;

import java.io.IOException;
import java.io.Writer;
import java.lang.annotation.Annotation;
import java.lang.reflect.Type;

import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.ext.Provider;

import com.google.gson.Gson;
import com.sun.jersey.spi.resource.Singleton;

/**
 * The JSON serializer that allows Java Objects to JSON transformation.
 *
 * @author Simone Tripodi
 * @version $Id: JSONObjectWriter.java 2 2009-07-04 14:28:38Z simone.tripodi $
 */
@Provider
@Produces(MediaType.APPLICATION_JSON)
@Singleton
public final class JSONObjectWriter extends AbstractObjectWriter {

    @Override
    protected void writeTo(Object obj, Class<?> type, Type genericType,
            Annotation[] annotations, MediaType mediaType,
            MultivaluedMap<String, Object> httpHeaders, Writer entityWriter)
            throws IOException, WebApplicationException {
        new Gson().toJson(obj, entityWriter);
        entityWriter.close();
    }

}
