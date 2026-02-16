# Journal Prompts API

## Project Overview

A simple, static JSON API serving AI-generated journaling prompts, hosted on GitHub Pages. The goal is to provide a free, fetchable endpoint for daily journal prompts that can be consumed by personal apps or other projects.

## Motivation

- No existing service provides a simple API for journal prompts
- Learning opportunity for the GitHub Pages + static API workflow
- Personal use case: integrate with another app/site for daily journaling

## Technical Specifications

### Stack
- **Hosting**: GitHub Pages (free, static hosting)
- **Data Format**: JSON
- **Scripting Language**: Python (for tooling/validation)

### API Design
- **Endpoint**: Single endpoint returning all prompts
- **Selection Method**: Random prompt selection (client-side)
- **Base URL**: https://mrafa3.github.io/journal-prompts/
- **API URL**: https://mrafa3.github.io/journal-prompts/journaling-prompts.json

### Data Schema

```json
{
  "prompts": [
    {
      "prompt": "What made you smile today?",
      "category": "reflection"
    }
  ]
}
```

**Categories:**
- reflection (daily reflection, appreciation, memorable moments)
- growth (goals, habits, challenges, learning)
- emotions (feelings, stress, self-care, boundaries)
- mindfulness (presence, curiosity, creative expression)
- parenting (gender/role-agnostic prompts for all parents)

### Scale
- 365+ unique prompts (full year of daily prompts)
- ~73 prompts per category

## Architecture

```
journal-prompts/
├── index.html              # Landing page with API docs + interactive demo
├── journaling-prompts.json # All prompts data (365+ entries)
├── scripts/
│   └── validate.py         # Validates JSON structure and counts
├── CLAUDE.md               # This file
└── README.md               # Project readme
```

The "API" is simply static JSON files served by GitHub Pages. Client-side JavaScript handles random selection when displaying prompts on the landing page.

## Deployment

Deployed via GitHub Pages (main branch, root folder).

- **Landing page**: https://mrafa3.github.io/journal-prompts/
- **API endpoint**: https://mrafa3.github.io/journal-prompts/journaling-prompts.json

## Validation

Run the validation script to check the JSON structure:

```bash
python scripts/validate.py
```

This will:
- Verify JSON is valid
- Count prompts per category
- Check for duplicate prompts
- Report any issues

## Usage Examples

### JavaScript
```javascript
const response = await fetch('https://mrafa3.github.io/journal-prompts/journaling-prompts.json');
const data = await response.json();
const randomPrompt = data.prompts[Math.floor(Math.random() * data.prompts.length)];
console.log(randomPrompt.prompt);
```

### Python
```python
import requests
import random

response = requests.get('https://mrafa3.github.io/journal-prompts/journaling-prompts.json')
prompts = response.json()['prompts']
daily_prompt = random.choice(prompts)
print(daily_prompt['prompt'])
```

### curl
```bash
curl -s https://mrafa3.github.io/journal-prompts/journaling-prompts.json | jq '.prompts | .[rand * length | floor]'
```
