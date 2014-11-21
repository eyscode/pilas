# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilasengine.actores.actor import Actor
import math

class DisparoLaser(Actor):
    """Muestra un disparo que avanza por la pantalla.
    
    .. image:: images/actores/disparo_laser.png

    Este actor se podría usar como arma para juegos de naves
    generalmente. Por ejemplo, el actor NaveRoja dispara usando
    este actor como munición.
    
    """

    def iniciar(self, x, y, rotacion, velocidad, imagen):
        self.x = x
        self.y = y
        self.rotacion = rotacion
        self.velocidad = velocidad
        self.imagen = imagen
        self._calcular_movimiento_desde_rotacion(velocidad)
        self.aprender(self.pilas.habilidades.EliminarseSiSaleDePantalla)

    
    def actualizar(self):
        self.x += self.dx
        self.y += self.dy
        
    def _calcular_movimiento_desde_rotacion(self, velocidad):
        rotacion_en_radianes = math.radians(self.rotacion)
        self.dx = math.cos(rotacion_en_radianes) * velocidad
        self.dy = math.sin(rotacion_en_radianes) * velocidad

