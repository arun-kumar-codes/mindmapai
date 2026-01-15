from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os
import tempfile

router = APIRouter()

@router.post("/export/pdf")
async def export_pdf(data: dict):
    try:
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, "Mind Map Export")
        p.drawString(100, 730, f"Title: {data.get('title', 'Untitled')}")
        p.drawString(100, 710, f"Content: {data.get('content', '')}")
        p.showPage()
        p.save()
        buffer.seek(0)
        return StreamingResponse(buffer, media_type='application/pdf', headers={"Content-Disposition": "attachment; filename=export.pdf"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/export/image")
async def export_image(data: dict):
    try:
        mind_map_image = Image.new('RGB', (800, 600), color = 'white')
        # Here you would draw the mind map on the image
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        mind_map_image.save(temp_file.name)
        return StreamingResponse(open(temp_file.name, mode="rb"), media_type="image/png", headers={"Content-Disposition": "attachment; filename=export.png"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/export/text")
async def export_text(data: dict):
    try:
        text_content = f"Title: {data.get('title', 'Untitled')}\nContent: {data.get('content', '')}"
        buffer = BytesIO(text_content.encode('utf-8'))
        return StreamingResponse(buffer, media_type='text/plain', headers={"Content-Disposition": "attachment; filename=export.txt"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))