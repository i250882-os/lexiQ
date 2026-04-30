# LexiQ

An Intelligent English vocabulary building app.

## Tech Stack

- **Python** | Django for backend API
- **JavaScript** | React for frontend UI

## Features

- [x] Read and paragraph and look up meanings
- [x] Remember user's weak words for quizes
- [x] Quizes

## Project Structure

```
lexiQ/
├── backend/          # Python backend code
├── frontend/         # React + Vite frontend
└── README.md         # This file
```

## Optimization
### HTTP Caching:
- Added HTTP caching using django utilities, endpoints like `/paragraph/<:id>` and `/word/<:word>` are called often with same arguments, so HTTP caching made a significant difference here.

**Effect**: Latency dropped to 0ms for subsequent requests.
<img width="508" height="60" alt="image" src="https://github.com/user-attachments/assets/e7c27ae8-e4da-4bef-8863-50ffb8cdff77" />


### Removed Unnecessary Dependencies + Lazy Loading:
- I was using `axios`, it was not really unnecessary, but gotta do optimization for the sidequest, so made my own simple `api` objects with `.get` and `.post` methods. Removing `axios` package coupled with LazyLoading in react made a drop in bundle size.

**Effect**: Bundle size reduced by 15%

### Size Before: 
<img width="230" height="100" alt="image" src="https://github.com/user-attachments/assets/5d32641f-f06f-4dbe-a841-59f861cbbf5d" />

### Size After:
<img width="259" height="184" alt="image" src="https://github.com/user-attachments/assets/14ab6a64-c86a-4195-91e0-d2231082c0c4" />

---

## Backend Django Apps:
- **Words** - Handels Paragraph, Lexeme and WordSense Models
- **Users** - Handels Login and Authentication.
- **Quiz** - Handlels Question, Option and Quiz models.

## Frontend Pages:
- **Home.jsx** - Landing page with instructions after login.
- **Paragraph.jsx** - Paragraph selector area, redirects to `read/` once paragraph is selected.
- **Read.jsx** - Main paragraph reading page with word details tabels.
- **Quiz.jsx** - Generate and Attempt quiz page.


## License

This project is open source and available under the MIT License.
