function(a) {
  var b = a.currentTarget,
    c = b.getAttribute("href");
  !c || c.startsWith("#") || "http:" !== b.protocol && "https:" !== b.protocol || (a = "IMG" === a.target.nodeName ? "Image" : "Link", c = b.getAttribute("data-za-element-name") || void 0, z.S.trackEvent(b, {
    action: "OpenUrl",
    element: a,
    element_name: c
  }, {
    link: {
      url: b.href
    }
  }))
}