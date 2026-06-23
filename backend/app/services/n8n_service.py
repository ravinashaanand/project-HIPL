"""N8N Integration Service"""

import requests
import logging
from typing import Dict, List, Any

from app.config import settings

logger = logging.getLogger(__name__)


class N8NService:
    """Service for N8N workflow integration"""
    
    def __init__(self):
        self.base_url = settings.N8N_URL
        self.api_key = settings.N8N_API_KEY
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}" if self.api_key else ""
        }
    
    def trigger_workflow(self, workflow_id: str, data: Dict[str, Any]) -> Dict:
        """
        Trigger N8N workflow
        
        Args:
            workflow_id: N8N workflow ID
            data: Input data for the workflow
        
        Returns:
            Response from N8N
        """
        try:
            webhook_url = f"{self.base_url}/webhook/workflow/{workflow_id}"
            response = requests.post(
                webhook_url,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            logger.info(f"✅ Workflow {workflow_id} triggered successfully")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"❌ Failed to trigger workflow {workflow_id}: {str(e)}")
            raise
    
    def get_workflow_status(self, workflow_id: str) -> Dict:
        """
        Get workflow execution status
        
        Args:
            workflow_id: N8N workflow ID
        
        Returns:
            Workflow status information
        """
        try:
            url = f"{self.base_url}/api/v1/workflows/{workflow_id}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"❌ Failed to get workflow status: {str(e)}")
            raise
    
    def list_workflows(self) -> List[Dict]:
        """
        List all workflows
        
        Returns:
            List of workflows
        """
        try:
            url = f"{self.base_url}/api/v1/workflows"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.RequestException as e:
            logger.error(f"❌ Failed to list workflows: {str(e)}")
            raise
    
    def execute_workflow(self, workflow_id: str, data: Dict[str, Any]) -> Dict:
        """
        Execute workflow synchronously
        
        Args:
            workflow_id: N8N workflow ID
            data: Input data
        
        Returns:
            Execution result
        """
        try:
            url = f"{self.base_url}/api/v1/workflows/{workflow_id}/execute"
            response = requests.post(
                url,
                json={"data": data},
                headers=self.headers,
                timeout=60
            )
            response.raise_for_status()
            logger.info(f"✅ Workflow {workflow_id} executed successfully")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"❌ Failed to execute workflow: {str(e)}")
            raise


# Create service instance
n8n_service = N8NService()
