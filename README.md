# LexiQ

An Intelligent English vocabulary building app. Leaning mathod based on scientific papers on learning vocabulary.

## How it works:
The idea is you read a selected paragraph, and when you feel that you dont know a word, instead of leaving the paragraph and using google etc etc. You can just move your cursor over the word to see its details, Then if you know that you would wanna learn this word, you can mark it as weak word by clicking on it, by doing that, when you take a quiz, the MCQs selection will prioritize MCQs based on your weak words. 

## Features
- [x] Read and paragraph and look up meanings
- [x] Remember user's weak words for quizes
- [x] Quizes
- [ ] Word Scoring

## Tech Stack
- `Python` | Django for backend API
- `JavaScript` | React for frontend UI

## Project Structure
```
lexiQ/
├── backend/          # Python backend code
├── frontend/         # React + Vite frontend
└── README.md         # This file
```

## Optimization
### HTTP Caching:
Added HTTP caching using django utilities, endpoints like `/paragraph/<:id>` and `/word/<:word>` are called often with same arguments, so HTTP caching made a significant difference here.

- **Effect**: Latency dropped to 0ms for subsequent requests.
<img width="508" height="60" alt="image" src="https://github.com/user-attachments/assets/e7c27ae8-e4da-4bef-8863-50ffb8cdff77" />

### Removed Unnecessary Dependencies + Lazy Loading:
I was using `axios`, it was not really unnecessary, but gotta do optimization for the sidequest, so made my own simple `api` objects with `.get` and `.post` methods. Removing `axios` package coupled with LazyLoading in react made a drop in bundle size.

- **Effect**: Bundle size reduced by 15%

### Size Comparison: 
<img width="230" height="100" alt="image" src="https://github.com/user-attachments/assets/5d32641f-f06f-4dbe-a841-59f861cbbf5d" />
-
<img width="259" height="184" alt="image" src="https://github.com/user-attachments/assets/14ab6a64-c86a-4195-91e0-d2231082c0c4" />

## Backend Django Apps:
- `Words` - Handels Paragraph, Lexeme and WordSense Models
- `Users` - Handels Login and Authentication.
- `Quiz` - Handlels Question, Option and Quiz models.

## Frontend Pages:
- `Home.jsx` - Landing page with instructions after login.
- `Paragraph.jsx` - Paragraph selector area, redirects to `read/` once paragraph is selected.
- `Read.jsx` - Main paragraph reading page with word details tabels.
- `Quiz.jsx` - Generate and Attempt quiz page.


## License

This project is open source and available under the MIT License.
