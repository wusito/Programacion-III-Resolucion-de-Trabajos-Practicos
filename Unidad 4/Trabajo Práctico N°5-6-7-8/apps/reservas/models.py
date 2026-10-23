from django.db import models
from django.utils import timezone 

# Create your models here.

# Modelo ActividadDeportiva
class ActividadDeportiva (models.Model):
    # Campos.
    nombre = models.CharField(
        max_length = 150, 
        verbose_name = "Nombre de la actividad"
    )
    
    descripcion = models.TextField(
        verbose_name = "Descripción de la actividad"
    )
    
    lugar = models.CharField(
        max_length = 200, 
        verbose_name = "Lugar donde se realiza"
    )
   
    cupo = models.IntegerField(
        verbose_name = "Cantidad máxima de participantes"
    )
    
    class Meta:
        verbose_name = "Actividad Deportiva"
        verbose_name_plural = "Actividades Deportivas"

    def __str__(self):
        return self.nombre



# Modelo Horario
class Horario (models.Model):
    # Campos.
    DIAS_SEMANA = [ # Limitar la elección del día según las opciones predefinidas.
        ("LU", "Lunes"),
        ("MA", "Martes"),
        ("MI", "Miércoles"),
        ("JU", "Jueves"),
        ("VI", "Viernes"),
        ("SA", "Sábado"),
        ("DO", "Domingo"),
    ]

    dia = models.CharField(
        max_length = 2, 
        choices = DIAS_SEMANA, 
        verbose_name = "Día de la semana"
    )
    
    hora_inicio = models.TimeField(
        verbose_name = "Hora de inicio"
    )
    
    hora_fin = models.TimeField(
        verbose_name = "Hora de finalización"
    )
    
    # Relación 1:N - Una actividad deportiva podrá tener varios horarios.
    actividad_deportiva = models.ForeignKey(
        ActividadDeportiva,
        on_delete = models.CASCADE,
        related_name = "horarios",
        verbose_name = "Actividad Deportiva",
    )

    def __str__(self):
        return f"{self.actividad_deportiva.nombre} - {self.get_dia_display()} ({self.hora_inicio} a {self.hora_fin})"

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"



# Modelo Inscripcion
class Inscripcion(models.Model):
    # Campos.
    ESTADOS_INSCRIPCION = [ # Limitar el estado según las opciones predefinidas.
        ("ACT", "Activa"),
        ("CAN", "Cancelada"),
    ]

    NIVELES_DEPORTIVOS = [
        ("inicial", "Inicial (Soy principiante)"),
        ("intermedio", "Intermedio (Tengo experiencia)"),
        ("avanzado", "Avanzado (Soy deportista — Compito)"),
    ]

    # Datos personales del formulario.
    nombre = models.CharField(
        max_length = 100, 
        verbose_name = "Nombre del participante"
    )
    
    apellido = models.CharField(
        max_length = 100, 
        verbose_name = "Apellido del participante"
        )
    
    dni = models.CharField( #Si una misma persona se inscribe a varias actividades, el DNI no debería ser unique=True.
        max_length = 8, 
        verbose_name = "Documento de identidad"
    )

    email = models.EmailField(
        verbose_name="Correo Electrónico", 
        blank=True, 
        null=True
    )
    
    telefono = models.CharField(
        max_length=20, 
        verbose_name="Teléfono", 
        blank=True, 
        null=True
    )
    
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de Nacimiento", 
        blank=True, 
        null=True
    )
    
    sexo = models.CharField(
        max_length=20, 
        verbose_name="Sexo", 
        blank=True, 
        null=True
    )


    # Información deportiva del formulario HTML
    experiencia_previa = models.BooleanField(
        default=False, 
        verbose_name="¿Posee Experiencia Previa?"
    )
    
    nivel_deportivo = models.CharField(
        max_length=20, 
        choices=NIVELES_DEPORTIVOS, 
        default="inicial", 
        verbose_name="Nivel Deportivo"
    )
    
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones"
    )
    
    # Datos administrativos de la inscripción
    fecha_inscripcion = models.DateField(
        default=timezone.now, 
        verbose_name="Fecha de registro"
    )

    estado = models.CharField(
        max_length=3,
        choices=ESTADOS_INSCRIPCION,
        default="ACT",
        verbose_name="Estado de la inscripción",
    )


    # Relación 1:1 - Cada inscripción deberá estar asociada a un horario.
    horario = models.ForeignKey(
        Horario,
        on_delete = models.CASCADE,
        related_name = "inscripciones",
        verbose_name = "Horario correspondiente",
    )

    def __str__(self):
        return (
            f"{self.apellido}, {self.nombre} - DNI: {self.dni} ({self.get_estado_display()})"
        )

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"