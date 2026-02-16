# Journal Prompts API

A free, static JSON API serving 365 journaling prompts, hosted on GitHub Pages.

**Live API**: https://mrafa3.github.io/journal-prompts/journaling-prompts.json

## Quick Start

Fetch a random prompt:

```javascript
const response = await fetch('https://mrafa3.github.io/journal-prompts/journaling-prompts.json');
const data = await response.json();
const prompt = data.prompts[Math.floor(Math.random() * data.prompts.length)];
console.log(prompt.prompt);
```

## Categories

- **reflection** - daily reflection, appreciation, memorable moments
- **growth** - goals, habits, challenges, learning
- **emotions** - feelings, stress, self-care, boundaries
- **mindfulness** - presence, curiosity, creative expression
- **parenting** - prompts for all parents

## Data Format

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

## Development

See [CLAUDE.md](CLAUDE.md) for project architecture and implementation details.

## License

MIT
