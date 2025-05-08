from typing import List, Optional
from datetime import datetime

from models.delivery_note import DeliveryNoteConstruction, DeliveryStatus
from repositories.delivery_repository import DeliveryRepository


class DeliveryService:
    """Service class containing business logic for delivery notes"""
    
    def __init__(self, repository: DeliveryRepository):
        self.repository = repository
    
    def get_all_delivery_notes(self) -> List[DeliveryNoteConstruction]:
        """Get all delivery notes"""
        return self.repository.get_all()
    
    def get_delivery_note_by_id(self, delivery_id: str) -> Optional[DeliveryNoteConstruction]:
        """Get a delivery note by its ID"""
        return self.repository.get_by_id(delivery_id)
    
    def create_delivery_note(self, note: DeliveryNoteConstruction) -> DeliveryNoteConstruction:
        """Create a new delivery note with validation"""
        # Set created_at time if not provided
        if not note.created_at:
            note.created_at = datetime.utcnow()
        
        # Calculate total quantity if not provided
        if note.total_quantity is None:
            note.total_quantity = sum(item.quantity_delivered for item in note.materials)
        
        # Set confirmed_at time if status is delivered
        if note.delivery_status == DeliveryStatus.delivered and note.confirmed_at is None:
            note.confirmed_at = datetime.utcnow()
        
        # Create and return the new note
        return self.repository.create(note)
    
    def update_delivery_note(self, delivery_id: str, note: DeliveryNoteConstruction) -> Optional[DeliveryNoteConstruction]:
        """Update an existing delivery note"""
        # Calculate total quantity if not provided
        if note.total_quantity is None:
            note.total_quantity = sum(item.quantity_delivered for item in note.materials)
        
        # Set confirmed_at time if status is delivered
        if note.delivery_status == DeliveryStatus.delivered and note.confirmed_at is None:
            note.confirmed_at = datetime.utcnow()
        
        # Update and return the note
        return self.repository.update(delivery_id, note)
    
    def update_delivery_status(self, delivery_id: str, status: DeliveryStatus) -> bool:
        """Update the status of a delivery note"""
        return self.repository.update_status(delivery_id, status)
    
    def delete_delivery_note(self, delivery_id: str) -> bool:
        """Delete a delivery note"""
        return self.repository.delete(delivery_id)
    
    def get_delivery_notes_by_project(self, project_id: str) -> List[DeliveryNoteConstruction]:
        """Get all delivery notes for a specific project"""
        all_notes = self.repository.get_all()
        return [note for note in all_notes if note.project.project_id == project_id]
    
    def get_delivery_notes_by_status(self, status: DeliveryStatus) -> List[DeliveryNoteConstruction]:
        """Get all delivery notes with a specific status"""
        all_notes = self.repository.get_all()
        return [note for note in all_notes if note.delivery_status == status] 