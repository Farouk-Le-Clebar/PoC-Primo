import { Component } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { RouterLink } from '@angular/router';


@Component({
  selector: 'app-selection',
  standalone: true,
  imports: [NavbarComponent, RouterLink],
  templateUrl: './selection.component.html',
  styleUrls: ['./selection.component.scss']
})

export class SelectionComponent {

}
