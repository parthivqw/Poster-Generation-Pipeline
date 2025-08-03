from pydantic import BaseModel
from typing import Optional, List

class PosterRequest(BaseModel):
    # Step 1: User's prompt about the kind of poster
    main_prompt: str

    # Step 2: Optional — background theme or vibe
    theme: Optional[str] = None  # If not given, let AI decide

    # Step 3: Fields selected by the user
    include_hero_headline: bool = False
    include_hero_subline: bool = False
    include_description: bool = False
    include_cta: bool = False
    include_testimonial: bool = False
    include_success_metrics: bool = False
    include_target_audience: bool = False
    include_cta_link: bool = False

    # Step 4: Optional — custom prompt override
    custom_prompt: Optional[str] = None

class PosterImageRequest(BaseModel):
    fields:dict #This will include hero_headline,description,etc..
    theme:Optional[str] = None # Can be user input ot LLaMa's suggestgion
