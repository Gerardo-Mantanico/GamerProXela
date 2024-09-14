import { ComponentFixture, TestBed } from '@angular/core/testing';

import  TarjetaDescuentoComponent  from './tarjeta-descuento.component';

describe('TarjetaDescuentoComponent', () => {
  let component: TarjetaDescuentoComponent;
  let fixture: ComponentFixture<TarjetaDescuentoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TarjetaDescuentoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TarjetaDescuentoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
