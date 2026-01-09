# app/models.py
from datetime import datetime
from typing import ClassVar

from pydantic import BaseModel, Field

# =====================================================
# REQUEST MODELS (lo que el cliente envía)
# =====================================================

class CreateEventRequest(BaseModel):
    """Request para crear un nuevo evento de intercambio"""
    names: list[str] = Field(..., min_length=3, description="Lista de participantes")


# =====================================================
# INTERNAL MODELS (estado interno del servidor)
# =====================================================

class Event(BaseModel):
    """Modelo del evento de intercambio"""
    id: str
    names: list[str]
    assignments: dict[str, str]  # {"giver": "receiver"}
    revealed_by: set[str] = Field(default_factory=set)
    created_at: datetime

    class Config:
        # Permite usar set en el modelo
        json_encoders: ClassVar = {
            set: list  # Convierte set a list en JSON
        }

    @property
    def all_revealed(self) -> bool:
        """Verifica si todos los participantes ya vieron su asignación"""
        return len(self.revealed_by) == len(self.names)


# =====================================================
# RESPONSE MODELS (lo que el servidor devuelve)
# =====================================================

class CreateEventResponse(BaseModel):
    """Respuesta al crear un evento"""
    event_id: str


class EventInfoResponse(BaseModel):
    """Respuesta con info general del evento (sin revelar asignaciones)"""
    total_participants: int
    revealed_count: int
    all_revealed: bool


class RevealAssignmentResponse(BaseModel):
    """Respuesta al revelar una asignación individual"""
    receiver: str
    all_revealed: bool


class CompleteListResponse(BaseModel):
    """Respuesta con la lista completa de asignaciones"""
    assignments: list[dict[str, str]]
