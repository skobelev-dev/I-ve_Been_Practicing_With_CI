from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import select, desc, asc, func, update

import schemas
from database import session
from models import Recipe
from fastapi.templating import Jinja2Templates
from loguru import logger

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.post('/recipes', response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.Recipe) -> schemas.Recipe:
    data = recipe.model_dump()
    data['ingredient_list'] = ', '.join(data.get('ingredient_list'))
    logger.info(f'{data}')
    new_recipe = Recipe(**data)
    async with session.begin():
        session.add(new_recipe)
    return schemas.Recipe.model_validate(new_recipe)


@router.get('/recipes', response_class=HTMLResponse)
async def get_all_recipes(request: Request):
    query = select(Recipe).order_by(desc(Recipe.views),
                                    asc(func.strftime('%M', Recipe.cooking_time)))
    result = await session.execute(query)
    recipes = result.scalars().all()
    context = {"request": request, "title": "Главная страница", 'recipes': recipes}
    return templates.TemplateResponse("index.html", context)


@router.get('/recipes/{idx}', response_class=HTMLResponse)
async def get_recipe(request: Request, idx: int = 1):
    query = select(Recipe).where(Recipe.id == idx)
    update_query = (
        update(Recipe)
        .where(Recipe.id == idx)
        .values(views=Recipe.views + 1)
    )
    result = await session.execute(query)
    await session.execute(update_query)
    await session.commit()
    recipe = result.scalar_one_or_none()
    context = {"request": request, "title": "Главная страница", 'recipe': recipe}
    return templates.TemplateResponse("recipe_info_by_id.html", context)