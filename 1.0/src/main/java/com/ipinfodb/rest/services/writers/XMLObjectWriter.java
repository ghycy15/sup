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
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.List;

import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.core.Response;
import javax.ws.rs.ext.Provider;

import org.apache.commons.betwixt.io.BeanWriter;
import org.apache.commons.betwixt.strategy.HyphenatedNameMapper;
import org.apache.commons.betwixt.strategy.NameMapper;

import com.sun.jersey.spi.resource.Singleton;

/**
 * The XML serializer that allows Java Objects to XML transformation.
 *
 * @author Simone Tripodi
 * @version $Id: XMLObjectWriter.java 23 2009-07-21 07:18:00Z simone.tripodi $
 */
@Provider
@Produces(MediaType.APPLICATION_XML)
@Singleton
public final class XMLObjectWriter extends AbstractObjectWriter {

    private static final char DEFAULT_PLURAL_POSTFIX = 's';

    private static final char EXCEPTION_PLURAL = 'y';

    private static final String EXCEPTION_PLURAL_POSTFIX = "ies";

    private final NameMapper nameMapper = new HyphenatedNameMapper();

    @Override
    protected void writeTo(Object obj, Class<?> type, Type genericType,
            Annotation[] annotations, MediaType mediaType,
            MultivaluedMap<String, Object> httpHeaders, Writer entityWriter)
            throws IOException, WebApplicationException {
        BeanWriter beanWriter = new BeanWriter(entityWriter);

        beanWriter.getBindingConfiguration().setMapIDs(false);
        beanWriter.getXMLIntrospector().getConfiguration().setElementNameMapper(this.nameMapper);

        try {
            if (List.class.isAssignableFrom(type)) {
                Type t = ((ParameterizedType) genericType).getActualTypeArguments()[0];
                String qualifiedName = ((Class<?>) t).getSimpleName();

                qualifiedName = this.nameMapper.mapTypeToElementName(qualifiedName);

                int index = qualifiedName.length() - 1;
                if (EXCEPTION_PLURAL == qualifiedName.charAt(index)) {
                    qualifiedName = qualifiedName.substring(0, index)
                        + EXCEPTION_PLURAL_POSTFIX;
                } else {
                    qualifiedName = qualifiedName + DEFAULT_PLURAL_POSTFIX;
                }

                if (this.getLog().isDebugEnabled()) {
                    this.getLog().debug("Rendering list Object: " + qualifiedName);
                }

                beanWriter.write(qualifiedName, obj);
            } else {
                beanWriter.write(obj);
            }
        } catch (Exception e) {
            throw new WebApplicationException(e, Response.Status.INTERNAL_SERVER_ERROR);
        } finally {
            entityWriter.close();
        }
    }

}
