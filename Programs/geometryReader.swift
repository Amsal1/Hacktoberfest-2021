var horizontalScrollCards: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 20) {
                ForEach(scrollCardData) { item in
                    GeometryReader { geo in
                        NavigationLink(destination: Text("Destination")) {
                            HorizontalScrollCards(scrollCardsData: item)
                                .rotation3DEffect(
                                    Angle(degrees: Double(geo.frame(in: .global).minX - 30) / -getAngleMultiplier(bounds: geo )),
                                    axis: (x: 0, y: 10, z: 0)
                                )
                        }
                    }
                    .frame(width: 280, height: 360)
                }
            }
            .padding(20)
            .padding(.bottom, 30)
        }
    }
