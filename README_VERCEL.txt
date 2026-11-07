VERCEL DEPLOYMENT (NO LOCAL PYTHON REQUIRED)

1. Extract this ZIP on your computer.
2. Create a GitHub repository at https://github.com/new
3. Upload the contents of this extracted folder to the repository (keep the folder structure).
4. Open https://vercel.com/new
5. Choose Import Git Repository and select the GitHub repository.
6. Keep the detected Python/Flask settings. Do not add a build command or output directory.
7. Click Deploy.

The Flask app is exposed as `app` in app.py. Static browser files are in `public/`, which Vercel serves from its CDN. The backend endpoint remains /api/analyze.

If Vercel asks for a framework override, choose Other only if Flask was not detected; leave build and output settings empty.
