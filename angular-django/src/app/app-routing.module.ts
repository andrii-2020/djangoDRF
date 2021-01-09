import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {OfficesComponent} from './components/offices/offices.component';
import {ReactiveFormsModule} from '@angular/forms';




const routes: Routes = [
  {
    path: 'offices', component: OfficesComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes), ReactiveFormsModule],
  declarations: [
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
