export default class Human {
  constructor(properties) {
    this.index = properties.index;
    this.name = this.generateName();
    this.skinTone = this.generateSkinTone();
    this.guilty = this.generateCrimes();
  }

  generateName = () => 'Jon';
  generateSkinTone = () => Math.random() >= 0.5 ? 'black' : 'white';
  generateCrimes = () => Math.random() >= 0.5;
}