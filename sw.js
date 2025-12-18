const CACHE_NAME = 'pwa-sample-cache-v1';
// キャッシュしたいファイルのリスト
// ここもリポジトリ名を含める必要があります
const urlsToCache = [
  '/pages/',
  '/pages/metricsgraph.html',
  'icon-192.png',
  'icon-512.png'
];

// インストール処理
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      })
  );
});

// リソースフェッチ時のキャッシュロード処理
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        return response ? response : fetch(event.request);
      })
  );
});
