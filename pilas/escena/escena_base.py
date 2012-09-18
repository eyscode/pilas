# -*- encoding: utf-8 -*-
# pilas engine - a video game framework.
#
# copyright 2010 - hugo ruscitti
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# website - http://www.pilas-engine.com.ar


class EscenaBase(object):
    def __init__(self):
        self.actores = []
        pass
    
    def iniciar(self):
        pass
    
    def limpiar(self):
        pass
    
    def pausar(self):
        pass
    
    def reanudar(self):
        pass
    
    def gestionar_eventos(self, events, parent):
        pass
    
    def actualizar(self):
        pass
    
    def dibujar(self):
        pass
