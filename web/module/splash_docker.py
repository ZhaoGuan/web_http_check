#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import docker


class DockerSplash:
    def __init__(self, proxy_port='8899', port="8050"):
        self.image = "scrapinghub/splash"
        self.docker = docker.from_env()
        self.port = port
        self.proxy_port = proxy_port
        self.docker_id = None

    def run(self):
        try:
            docker_id = self.docker.containers.run(self.image,
                                                   environment={
                                                       "HTTP_PROXY": "http://192.168.100.27:{}".format(
                                                           str(self.proxy_port)),
                                                       "HTTPS_PROXY": "http://192.168.100.27:{}".format(
                                                           str(self.proxy_port)),
                                                       "http_proxy": "http://192.168.100.27:{}".format(
                                                           str(self.proxy_port)),
                                                       "https_proxy": "http://192.168.100.27:{}".format(
                                                           str(self.proxy_port))
                                                   },
                                                   ports={"8050": str(self.port)},
                                                   remove=True,
                                                   detach=True).id
            self.docker_id = docker_id
        except Exception as e:
            print(e)
            assert False, "splash启动失败"

    def splash_status(self):
        return self.docker.containers.get(self.docker_id).status

    def splash_close(self):
        container = self.docker.containers.get(self.docker_id)
        container.kill()
