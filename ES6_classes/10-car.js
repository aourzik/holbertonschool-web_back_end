export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  // brand
  get brand() {
    return this._brand;
  }

  set brand(value) {
    this._brand = value;
  }

  // motor
  get motor() {
    return this._motor;
  }

  set motor(value) {
    this._motor = value;
  }

  // color
  get color() {
    return this._color;
  }

  set color(value) {
    this._color = value;
  }

  // important: permet aux classes enfants de se cloner correctement
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const C = this.constructor[Symbol.species];
    return new C();
  }
}