import json
import os
from typing import List, Optional, Dict, Any
from datetime import datetime
from models.delivery_note import DeliveryNoteConstruction, DeliveryStatus


class DeliveryRepository:
    """Repository class for managing delivery notes data persistence"""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self._ensure_data_file_exists()
    
    def _ensure_data_file_exists(self):
        """Make sure the data file exists, create it if it doesn't"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)
    
    def _load_data(self) -> List[Dict[str, Any]]:
        """Load all delivery notes from the data file"""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    
    def _save_data(self, data: List[Dict[str, Any]]):
        """Save delivery notes data to the data file"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=self._handle_datetime)
    
    def _handle_datetime(self, obj):
        """Helper method to serialize datetime objects to ISO format"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    def get_all(self) -> List[DeliveryNoteConstruction]:
        """Get all delivery notes"""
        data = self._load_data()
        return [DeliveryNoteConstruction.parse_obj(item) for item in data]
    
    def get_by_id(self, delivery_id: str) -> Optional[DeliveryNoteConstruction]:
        """Get a delivery note by its ID"""
        data = self._load_data()
        for item in data:
            if item.get('delivery_note_id') == delivery_id:
                return DeliveryNoteConstruction.parse_obj(item)
        return None
    
    def create(self, note: DeliveryNoteConstruction) -> DeliveryNoteConstruction:
        """Create a new delivery note"""
        data = self._load_data()
        
        # Check for duplicate ID
        if any(item.get('delivery_note_id') == note.delivery_note_id for item in data):
            raise ValueError(f"Delivery note with ID {note.delivery_note_id} already exists")
        
        # Add new note
        data.append(note.dict(by_alias=True))
        self._save_data(data)
        return note
    
    def update(self, delivery_id: str, note: DeliveryNoteConstruction) -> Optional[DeliveryNoteConstruction]:
        """Update an existing delivery note"""
        data = self._load_data()
        
        for i, item in enumerate(data):
            if item.get('delivery_note_id') == delivery_id:
                # Update the existing note
                data[i] = note.dict(by_alias=True)
                self._save_data(data)
                return note
        
        return None  # Note not found
    
    def update_status(self, delivery_id: str, status: DeliveryStatus) -> bool:
        """Update just the status of a delivery note"""
        data = self._load_data()
        
        for i, item in enumerate(data):
            if item.get('delivery_note_id') == delivery_id:
                # Update just the status
                data[i]['delivery_status'] = status
                if status == DeliveryStatus.delivered:
                    data[i]['confirmed_at'] = datetime.utcnow().isoformat()
                self._save_data(data)
                return True
        
        return False  # Note not found
    
    def delete(self, delivery_id: str) -> bool:
        """Delete a delivery note by ID"""
        data = self._load_data()
        initial_length = len(data)
        
        data = [item for item in data if item.get('delivery_note_id') != delivery_id]
        
        if len(data) < initial_length:
            self._save_data(data)
            return True
            
        return False  # Note not found 