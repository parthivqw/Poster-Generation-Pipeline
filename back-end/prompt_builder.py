def build_image_generation_prompt(fields: dict, theme: str = None) -> str:
    """
    Dynamically constructs an image generation prompt for a poster based on selected fields.

    Args:
        fields (dict): Dictionary with keys like 'hero_headline', 'description', etc.
        theme (str, optional): The suggested or user-provided background theme.

    Returns:
        str: Fully assembled image generation prompt ready for image model.
    """

    layout_lines = []

    if 'hero_headline' in fields:
        layout_lines.append(f'- Top center: Large bold heading — "{fields["hero_headline"]}"')

    if 'hero_subline' in fields:
        layout_lines.append(f'- Just below: Smaller subheading — "{fields["hero_subline"]}"')

    if 'description' in fields:
        layout_lines.append(f'- Center area: Short paragraph — "{fields["description"]}"')

    if 'success_metrics' in fields:
        layout_lines.append(f'- Bottom left: Compact highlight of achievements — "{fields["success_metrics"]}"')

    if 'target_audience' in fields:
        layout_lines.append(f'- Bottom right: Brief audience description — "{fields["target_audience"]}"')

    if 'testimonial' in fields:
        layout_lines.append(f'- Lower section: Italicized quote — "{fields["testimonial"]}"')

    if 'cta' in fields:
        layout_lines.append(f'- Bottom center: Button with the text — "{fields["cta"]}"')
    
    if 'cta_link' in fields:
        layout_lines.append(f'- Very bottom: Minimal hyperlink — "{fields["cta_link"]}"')

    layout_block = "\n".join(layout_lines)

    theme_block = theme or "A modern, professional tech-themed poster background with subtle digital code and soft gradients."

    full_prompt = f"""
Design a premium 1024x1024 promotional poster for a Java Bootcamp.

📐 Layout:
{layout_block}

🧠 Critical Instructions:
- Do **not** include any field labels like “Success Metrics”, “Target Audience”, or “Testimonial”.
- The text should appear *naturally* as part of the poster design — not as form layout or metadata.
- Treat all text elements as part of the visual composition.
- Avoid overlapping, distortion, and gibberish. Fonts must be clean, sans-serif, and fully legible.

🎨 Background Theme:
{theme_block}

🖋 Typography & Composition:
- All fonts should be bold, sans-serif, and clean
- Text must be perfectly legible and free of distortion
- Layout should feel like a real-world marketing poster with white space, balance, and hierarchy
- No gibberish text, no overlapping elements, and absolutely no field names shown on the poster
    """

    return full_prompt.strip()
