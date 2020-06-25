import React from 'react';
import * as d3 from 'd3';
import styles from './style';

export default class Narrator extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { text1: React.createRef(), text2: React.createRef() };
  }

  componentDidMount() {
    this.animate();
  }

  componentDidUpdate() {
    this.animate();
  }

  animate() {
    switch (this.props.phase) {
      case 1:
        this.animatePhase1();
        break;
      case 2:
        this.animatePhase2();
        break;
      default:
        this.animatePhase1();
    }
  }

  animatePhase1() {
    const { duration} = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = timePerStep * 0.5;
    const animationTime = timePerStep * 0.25;

    d3.select(this.references.text1.current)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Een fictieve populatie van 100 mensen')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn wit')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn zwart')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn crimineel')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      // scenario 1
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 1)
      .text('De politie controleert willekeurig.')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0);

      // scenario 2
      // .transition()
      // .delay(delay)
      // .duration(animationTime)
      // .style('opacity', 1)
      // .text('De politie controleert vaker in "zwarte" buurten.')
      // .transition()
      // .delay(delay)
      // .duration(animationTime)
      // .style('opacity', 0);

      // scenario 3
      // .transition()
      // .delay(delay)
      // .duration(animationTime)
      // .style('opacity', 1)
      // .text('De politie controleert vaker in "zwarte" buurten...')
      // .transition()
      // .delay(delay)
      // .duration(animationTime)
      // .style('opacity', 0)

      // .transition()
      // .duration(animationTime)
      // .style('opacity', 1)
      // .text('...én heeft een bias.')
      // .transition()
      // .delay(delay)
      // .duration(animationTime)
      // .style('opacity', 0)
  }


  animatePhase2() {
    const { duration} = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = timePerStep * 0.5;
    const animationTime = timePerStep * 0.25;

    d3.select(this.references.text2.current)
      .style('opacity', 0)

      .transition()
      .delay(delay * 2)
      .duration(animationTime)
      .style('opacity', 1)
      .text('Dit zijn de gecontroleerde mensen.')
      .transition()
      .delay(delay * 0.8)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('De politie telt het aantal criminelen van elke huidskleur.')
      .transition()
      .delay(delay * 0.8)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Dit is de totale verdeling van criminelen per huidskleur:')
      .transition()
      .delay(delay * 0.8)
      .duration(animationTime)
      .style('opacity', 0)
  }

  render() {
    return (
      <g>
        <text ref={this.references.text1} style={styles.text}
          className='narrator'
          x='50%'
          y='50%'
        />
        <text ref={this.references.text2} style={styles.text2}
          className='narrator'
          x='50%'
          y='50%'
        />
      </g>
    );
  }
}
