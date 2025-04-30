#!/bin/bash

set -e

uv run reflex export --frontend-only --env prod
unzip frontend.zip -d frontend
rm frontend.zip

# frontend/index.html にある `"/_next` を `"./_next"` に変更
sed -i '' 's/\/_next/\.\/_next/g' frontend/index.html
sed -i '' 's/\/_next/\.\/_next/g' frontend/404.html

# 画像リンクを相対パスに変更
sed -i '' -E 's/img(.*) src="\//img\1 src=".\//g' frontend/index.html
sed -i '' -E 's/img(.*) src="\//img\1 src=".\//g' frontend/404.html
sed -i '' -E 's/src:"\//src:"\.\//g' frontend/_next/static/chunks/pages/index*.js
sed -i '' -E 's/src:e\.image_src/src:"\.\/"\+e\.image_src/g' frontend/_next/static/chunks/pages/index*.js

# ws のエラーを握りつぶす (使わないので)
sed -i '' 's/,this\.ws\.onerror=e=>this\.onError("websocket error",e)//g' frontend/_next/static/chunks/pages/_app*.js
