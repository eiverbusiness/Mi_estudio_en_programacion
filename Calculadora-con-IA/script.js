const display = document.getElementById("display");
let current = "";

function updateDisplay(value) {
  display.value = value || "0";

  const length = display.value.length;
  if (length > 12) {
    display.style.fontSize = `${Math.max(1.1, 3.25 - (length - 12) * 0.16)}rem`;
  } else {
    display.style.fontSize = "";
  }
}

function calculate(expression) {
  try {
    const sanitized = expression
      .replace(/×/g, "*")
      .replace(/÷/g, "/")
      .replace(/√\(/g, "Math.sqrt(")
      .replace(/π/g, "Math.PI")
      .replace(/\^/g, "**");

    const result = Function(`"use strict"; return (${sanitized})`)();
    return Number.isFinite(result) ? result : "Error";
  } catch {
    return "Error";
  }
}

function handleButton(button) {
  const value = button.dataset.value;
  const action = button.dataset.action;

  if (action === "clear") {
    current = "";
    updateDisplay(current);
    return;
  }

  if (action === "delete") {
    current = current.slice(0, -1);
    updateDisplay(current);
    return;
  }

  if (action === "calculate") {
    const result = calculate(current);
    current = result === "Error" ? "" : String(result);
    updateDisplay(result);
    return;
  }

if (action === "sqrt") {
    if (current.length === 0 || /[+\-*/%^]$/.test(current)) {
    current += "√(";
    } else {
    current += "*√(";
    }

    updateDisplay(current);
    return;
}

  if (action === "square") {
    if (current.length > 0 && !/[+\-*/%^]$/.test(current)) {
      current += "**2";
      updateDisplay(current);
    }
    return;
  }

  if (value) {
    if (value === "." && current.slice(-1) === ".") {
      return;
    }

    current += value;
    updateDisplay(current);
  }
}

const buttons = document.querySelectorAll(".btn");
buttons.forEach((button) => {
  button.addEventListener("click", () => handleButton(button));
});

window.addEventListener("keydown", (event) => {
  const key = event.key;
  const allowed = "0123456789.+-*/%^()";

  if (key.toLowerCase() === "p") {
    event.preventDefault();
    current += "π";
    updateDisplay(current);
    return;
  }

  if (allowed.includes(key)) {
    event.preventDefault();
    current += key;
    updateDisplay(current);
    return;
  }

  if (key === "Enter" || key === "=") {
    event.preventDefault();
    const result = calculate(current);
    current = result === "Error" ? "" : String(result);
    updateDisplay(result);
    return;
  }

  if (key === "Backspace") {
    event.preventDefault();
    current = current.slice(0, -1);
    updateDisplay(current);
    return;
  }

  if (key.toLowerCase() === "c") {
    event.preventDefault();
    current = "";
    updateDisplay(current);
  }
});
