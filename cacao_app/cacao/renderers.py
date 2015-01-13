# -*- coding: utf-8 -*-
import logging
import mimetypes
import os
import hashlib

from django.conf import settings
from django.test.client import Client
from django.core.urlresolvers import reverse

from django_perseus.exceptions import RendererException
from django_perseus.renderers.base import BaseRenderer

from .models import Guide, Content

logger = logging.getLogger('perseus')

class GuideRenderer(BaseRenderer):
    def render_path(self, path=None, view=None):
        if path:
            # create deploy dir if not exists
            deploy_dir = settings.PERSEUS_SOURCE_DIR
            outpath = os.path.join(deploy_dir, '')
            if not os.path.exists(deploy_dir):
                os.makedirs(deploy_dir)

            # create the renders page
            if path == '/':
                response, mime = self.render_page(path)
                outpath = os.path.join(outpath, 'index{0}'.format(mime))
                self.save_page(response, outpath)
                return
            else:
                response, mime = self.render_page(path)
                name = '%s.html' % hashlib.sha1(path).hexdigest()
                outpath = os.path.join(deploy_dir, name)            
                self.save_page(response, outpath)
                return
            

    def render_page(self, path):
        response = self.client.get(path)
        if response.status_code is not 200:
            raise RendererException(
                'Path: {0} returns status code: {1}.'.format(path, response.status_code))
        return response, self.get_mime(response)

    def get_mime(self, response):
        mime = response['Content-Type']
        encoding = mime.split(';', 1)[0]
        return mimetypes.guess_extension(encoding)

    def save_page(self, response, outpath):
        logger.debug(outpath)
        with open(outpath, 'wb') as f:
            f.write(response.content)

    def generate(self):
        self.client = Client()
        for path in self.paths():
            self.render_path(path=path)


class HomeRenderer(GuideRenderer):
    def paths(self):
        paths = set([])
        guides = Guide.objects.all()
        for guide in guides:
            paths.add(guide.get_absolute_url())
        contents = Content.objects.all()
        for content in contents:
            paths.add(content.get_absolute_url())

        return paths


renderers = [HomeRenderer, ]