.pragma library

// Aspect buckets for the connected screen, not hardcoded connector names.
// laptop  ~16:10 (1.6)
// wide    ~16:9  (1.778)
// ultrawide 21:9+ / 2.4:1 (>= 2.1)

function aspect(w, h) {
  if (!h) return 0
  return w / h
}

function bucket(w, h) {
  var a = aspect(w, h)
  if (a >= 2.1) return "ultrawide"
  if (a >= 1.70) return "wide"
  return "laptop"
}

function covers(imageW, imageH, screenW, screenH) {
  return imageW >= screenW && imageH >= screenH
}

function fits(imageW, imageH, screenW, screenH) {
  if (!covers(imageW, imageH, screenW, screenH)) return false
  var screenBucket = bucket(screenW, screenH)
  if (screenBucket === "laptop") return true
  return bucket(imageW, imageH) === screenBucket
}
