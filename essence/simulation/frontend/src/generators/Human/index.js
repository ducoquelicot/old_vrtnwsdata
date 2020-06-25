import rng from './numgen'

export default class Human {
  constructor(properties) {
    this.index = properties.index;
    this.name = this.generateName();
    this.skinTone = this.generateSkinTone();
    this.guilty = this.generateCrimes();
    this.control = this.generateChance();
    // this.control = undefined
  }

  generateName = () => 'Jon';
  generateSkinTone = () => rng() >= 0.5 ? 'black' : 'white';
  generateCrimes = () => rng() >= 0.5;

  // scenario 1
  generateChance = () => Math.random() >= 0.5;

  // scenario 2
  // generateChance = function() {
  //   if (this.skinTone === 'black') {
  //     return Math.random() >= 0.3;
  //   }
  //   else {
  //     return Math.random() >= 0.7;
  //   }
  // }

}