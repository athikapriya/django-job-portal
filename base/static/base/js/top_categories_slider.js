// top categories slider

document.addEventListener("DOMContentLoaded", () => {
  const sliderRow = document.querySelector("#top-categories .row:nth-of-type(2)");
  if (!sliderRow) return;

  const originals = Array.from(sliderRow.children);
  const total = originals.length;

  // ✅ Duplicate all items once for smooth looping
  originals.forEach((item) => {
    const clone = item.cloneNode(true);
    sliderRow.appendChild(clone);
  });

  // ✅ Layout styling
  sliderRow.style.display = "flex";
  sliderRow.style.flexWrap = "nowrap";
  sliderRow.style.overflowX = "hidden";
  sliderRow.style.overflowY = "hidden";
  sliderRow.style.scrollBehavior = "auto"; // disable browser's smooth scroll, we’ll handle it manually

  let itemWidth = originals[0].offsetWidth;
  let scrollPosition = 0;
  let isResetting = false;

  function slideNext() {
    if (isResetting) return; // prevent running during reset

    scrollPosition += itemWidth;

    // Instantly reset if reaching the clone end
    if (scrollPosition >= itemWidth * total) {
      isResetting = true;
      sliderRow.scrollLeft = 0; // instant reset, no animation
      scrollPosition = itemWidth; // jump to 2nd item smoothly
      requestAnimationFrame(() => {
        sliderRow.scrollTo({ left: scrollPosition, behavior: "smooth" });
        isResetting = false;
      });
    } else {
      sliderRow.scrollTo({ left: scrollPosition, behavior: "smooth" });
    }
  }

  // ✅ Auto slide every 5 seconds
  let autoSlide = setInterval(slideNext, 5000);

  function stopAutoSlide() {
    clearInterval(autoSlide);
  }

  function startAutoSlide() {
    stopAutoSlide();
    autoSlide = setInterval(slideNext, 5000);
  }

  // ✅ Swipe/Drag support
  let isDragging = false;
  let startX, scrollLeft;

  sliderRow.addEventListener("mousedown", (e) => {
    isDragging = true;
    startX = e.pageX - sliderRow.offsetLeft;
    scrollLeft = sliderRow.scrollLeft;
    stopAutoSlide();
  });

  sliderRow.addEventListener("mouseleave", () => {
    isDragging = false;
    startAutoSlide();
  });

  sliderRow.addEventListener("mouseup", () => {
    isDragging = false;
    startAutoSlide();
  });

  sliderRow.addEventListener("mousemove", (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - sliderRow.offsetLeft;
    const walk = (x - startX) * 1.5;
    sliderRow.scrollLeft = scrollLeft - walk;
  });

  // ✅ Touch (mobile)
  sliderRow.addEventListener("touchstart", (e) => {
    startX = e.touches[0].clientX;
    scrollLeft = sliderRow.scrollLeft;
    stopAutoSlide();
  });

  sliderRow.addEventListener("touchmove", (e) => {
    const x = e.touches[0].clientX;
    const walk = (x - startX) * 1.5;
    sliderRow.scrollLeft = scrollLeft - walk;
  });

  sliderRow.addEventListener("touchend", startAutoSlide);

  // ✅ Responsive fix
  window.addEventListener("resize", () => {
    itemWidth = originals[0].offsetWidth;
  });
});
