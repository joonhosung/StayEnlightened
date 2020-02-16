# MERN Stack Web App hosted on Google Cloud App Engine for NodeJS



## Local Dev/Testing Instructions
1. Modify the `webapp/client/src/api/index.js` to use `localhost` by uncommenting out the testing `baseURL` and commenting out the production `baseURL`. It should end up looking like:

```javascript
baseURL: 'http://localhost:3000/api',
```

2. Start the local backend and front end
```bash
cd server && npm start
cd ..
cd client && npm start
```



## Deploying new services on Google Cloud
1. Modify the `webapp/client/src/api/index.js` and do the opposite; use the actual backend api path by uncommenting out the production `baseURL` and commenting out the testing `baseURL`. It should look like:

```javascript
baseURL: 'https://server-dot-stayenlightenedv2.appspot.com/api',
```

2. Go on Google Cloud App Engine and start the `server` and `client` as single services

```bash
cd server
gcloud app deploy server.yaml
```

```bash
cd client
gcloud app deploy client.yaml
```



## Adding New Pages
1. Add new route to `client/src/app/index.js`
2. Create new page component in `client/src/pages`
3. (Optional) Add path of new page to `client/src/components/Links.jsx` to get new button in `NavBar`



## Creating New API Links (backend only)
1. Add new route to `server/routes/studyspace-router.js`

2. Add `async` function for new request function access database in `server/controllers/studyspace-ctrl.js`



## Using New API Links (linking backend to to frontend)
1. Add new function to access api in `client/src/api/index.js`
2. import new api function wherever and front end and use as desired
